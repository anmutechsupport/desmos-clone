import math 

fs = 100
scaleFactor = 20 
h = 800
w = 800
dx = w/fs

# Initialize slider positions and parameter values
sliderX = [50, 50, 50, 50]
adjustment = [0, 0, 0, 0]
sliderLabels = ["a", "k", "d", "c"]

# Initialize radio global variables
radioSin, radioQuadratic, radioLinear, radioExponential = False, False, False, False
radPosX = 600

def colorWheel(funcName, prop="fill"): # function to dynamically change element colors 
    if prop == "fill":
        if funcName == "sin":
            fill(255, 0, 0)
        if funcName == "quadratic":
            fill(0, 255, 0)
        if funcName == "linear":
            fill(0, 0, 255)
        if funcName == "exponential":
            fill(255, 255, 0)
    if prop == "stroke":
        if funcName == "sin":
            stroke(255, 0, 0)
        if funcName == "quadratic":
            stroke(0, 255, 0)
        if funcName == "linear":
            stroke(0, 0, 255)
        if funcName == "exponential":
            stroke(255, 255, 0)

def setup():
    global radioSin, radioQuadratic, radioLinear, radioExponential
    
    size(h, w)  
    # Set initial radio button states
    radioSin = True

    # Initialize sliders with range, initial value, and step size
    for i in range(4):
        sliderX[i] += i * 100
        adjustment[i] = 1.0 * (sliderX[i] - 50) / (350 - 50) # [0.0, 1.0] initialization, uses formula for normalizing values between 0 and 1, z = (x-min)/(max-min)
        # print(adjustment[i])

def draw():
    global radioSin, radioQuadratic, radioLinear, radioExponential
    global sliderX, adjustment

    background(255)
    drawGrid()
    drawAxes()

    # Get the current value of the sliders
    a = adjustment[0]*20 - 10  # scale adjustment to [-10, 10]
    k = adjustment[1]*20 - 10
    d = adjustment[2]*20 - 10
    c = adjustment[3]*20 - 10

    # Draw the corresponding graph based on which radio button is selected
    if radioSin:
        sin(a, k, d, c)
    elif radioQuadratic:
        quadratic(a, k, d, c)
    elif radioLinear:
        linear(a, k, d, c)
    elif radioExponential:
        exponential(a, k, d, c)

    drawRadioButtons()
      
    drawSliders()  # draw sliders last so they appear on top of the functions

def mouseClicked():
    global radioSin, radioQuadratic, radioLinear, radioExponential

    global sliderX, adjustment

    for i in range(4):
        if mouseX >= 50 and mouseX <= 350 and mouseY >= 40 + i * 50 and mouseY <= 60 + i * 50:
            sliderX[i] = mouseX
            adjustment[i] = 1.0 * (sliderX[i] - 50) / (350 - 50) # adjustment values are always between 0 and 1 

    # Add logic to change the radio button state when one is clicked
    # The radio buttons are assumed to be drawn at the following specific coordinates:
    r = 10  # radius of radio buttons
    if dist(mouseX, mouseY, radPosX, 50) < r:
        radioSin = True
        radioQuadratic = False
        radioLinear = False
        radioExponential = False
    elif dist(mouseX, mouseY, radPosX, 80) < r:
        radioSin = False
        radioQuadratic = True
        radioLinear = False
        radioExponential = False
    elif dist(mouseX, mouseY, radPosX, 110) < r:
        radioSin = False
        radioQuadratic = False
        radioLinear = True
        radioExponential = False
    elif dist(mouseX, mouseY, radPosX, 140) < r:
        radioSin = False
        radioQuadratic = False
        radioLinear = False
        radioExponential = True

def mouseDragged():
    global sliderX, adjustment

    for i in range(4):
        if mouseX >= 50 and mouseX <= 350 and mouseY >= 40 + i * 50 and mouseY <= 60 + i * 50: # checks which slider is being dragged based on height
            sliderX[i] = mouseX
            adjustment[i] = 1.0 * (sliderX[i] - 50) / (350 - 50)

# drawing sliders
def drawSliders():
    global sliderX, sliderLabels

    # Draw the box first so it's underneath the sliders
    fill(255, 255, 255, 150)  # semi-transparent white fill
    rectMode(CORNER)  # Switch to CORNER mode
    rect(30, 20, 400, 210)  # Draw a rectangle to enclose the sliders

    strokeWeight(3)
    stroke(0)

    for i in range(4):
        fill(100)
        line(50, 50 + i * 50, 350, 50 + i * 50)
        line(50, 40 + i * 50, 50, 60 + i * 50)
        line(350, 40 + i * 50, 350, 60 + i * 50)
        rectMode(CENTER)  # Switch back to CENTER mode for the sliders
        rect(sliderX[i], 50 + i * 50, 10, 30)
        fill(0)
        text(sliderLabels[i] + ": " + str(round(adjustment[i]*20 - 10, 1)), 360, 53 + i * 50)
        noFill()


def drawGrid():
    stroke(200)  # Set the grid color to light gray
    # Draw vertical lines
    for i in range(0, width, scaleFactor):  # Adjust the third parameter to change the grid size
        line(i, 0, i, height)
    # Draw horizontal lines
    for i in range(0, height, scaleFactor):  # Adjust the third parameter to change the grid size
        line(0, i, width, i)

def drawAxes():
    stroke(0)  # Set the axes color to black
    strokeWeight(2)  # Set the axes thickness
    # Draw the x-axis
    line(0, height / 2, width, height / 2)
    # Draw the y-axis
    line(width / 2, 0, width / 2, height)

def sin(a=1, k=1, d=0, c=0):
    beginShape()
    colorWheel("sin", "stroke")
    noFill()  # Specify no fill
    x = 0
    y = (-1*a*math.sin(k*(1.0/scaleFactor*(x-width/2)-d))-c)*scaleFactor + height/2 # reflect across x-axis since x increments go from top to bottom of window, scale output by scaleFactor, vertically shift by height/2 to start from y=0
    curveVertex(x, y)  # Additional vertex for smooth curve
    
    for i in range(fs):
        x = i*dx
        # print(x)
        # print(k*((x-width/2.0)/scaleFactor-d)) # divide shifted x by scaleFactor since exactly scaleFactor number of pixels make up a unit on the graph 
        y = (-1*a*math.sin(k*(1.0/scaleFactor*(x-width/2)-d))-c)*scaleFactor + height/2 # input to sine should be a float value 
        # print(y)
        curveVertex(x, y)
    
    x = (fs-1)*dx
    y = (-1*a*math.sin(k*(1.0/scaleFactor*(x-width/2)-d))-c)*scaleFactor + height/2
    curveVertex(x, y)  # Additional vertex for smooth curve
    endShape()

def quadratic(a=1, k=1, d=0, c=0):
    colorWheel("quadratic", "stroke")
    beginShape()
    noFill()

    # Additional vertex for smooth curve at the start
    x = 0
    # y = (-a*((1.0/scaleFactor*(x-width/2))**2)+b*(1.0/scaleFactor*(x-width/2))+c)*scaleFactor + height/2
    y = (-a*k*(1.0/scaleFactor*(x-width/2)-d)**2-c)*scaleFactor + height/2 
    curveVertex(x, y)
    
    for i in range(fs):
        x = i*dx
        y = (-a*k*(1.0/scaleFactor*(x-width/2)-d)**2-c)*scaleFactor + height/2 
        curveVertex(x, y)
    
    # Additional vertex for smooth curve at the end
    x = (fs-1)*dx
    y = (-a*k*(1.0/scaleFactor*(x-width/2)-d)**2-c)*scaleFactor + height/2 
    curveVertex(x, y) 

    endShape()

def linear(a, k, d, c):
    beginShape()
    colorWheel("linear", "stroke")
    noFill()
    for i in range(fs):
        x = i*dx 
        # y = (-m*(1.0/scaleFactor*(x-width/2))+b)*scaleFactor + height/2
        y = (-a*k*(1.0/scaleFactor*(x-width/2)-d)-c) * scaleFactor + height/2
        curveVertex(x, y)

    endShape()

def exponential(a=1, k=1, d=0, c=0):
    beginShape()
    colorWheel("exponential", "stroke")
    noFill()  # Specify no fill

    # Additional vertex for smooth curve at the start
    x = 0
    # y = (-a*b**(k*(1.0/scaleFactor*(x-width/2)-d))+c)*scaleFactor + height/2
    y = (-a*2**(k*(1.0/scaleFactor*(x-width/2)-d))-c)*scaleFactor + height/2
    curveVertex(x, y)

    for i in range(fs):
        x = i*dx
        y = (-a*2**(k*(1.0/scaleFactor*(x-width/2)-d))-c)*scaleFactor + height/2
        curveVertex(x, y)
    
    # Additional vertex for smooth curve at the end
    x = (fs-1)*dx
    y = (-a*2**(k*(1.0/scaleFactor*(x-width/2)-d))-c)*scaleFactor + height/2
    curveVertex(x, y)  

    endShape()

def drawRadioButtons():
    global radPosX

    # Draw the box first so it's underneath the radio buttons
    fill(255, 255, 255, 150)  # semi-transparent white fill
    rectMode(CORNER)  # Switch to CORNER mode
    rect(radPosX-30, 20, 200, 150)  # Draw a rectangle to enclose the radio buttons

    fill(200)
    stroke(0)
    ellipse(radPosX, 50, 20, 20)  # sin
    ellipse(radPosX, 80, 20, 20)  # quadratic
    ellipse(radPosX, 110, 20, 20)  # linear
    ellipse(radPosX, 140, 20, 20)  # exponential
    
    textSize(16)
    colorWheel("sin")
    text("sin", radPosX+50, 50)
    colorWheel("quadratic")
    text("quadratic", radPosX+50, 80)
    colorWheel("linear")
    text("linear", radPosX+50, 110)
    colorWheel("exponential")
    text("exponential", radPosX+50, 140)

    # fill(150)
    if radioSin:
        colorWheel("sin")
        ellipse(radPosX, 50, 10, 10)
    elif radioQuadratic:
        colorWheel("quadratic")
        ellipse(radPosX, 80, 10, 10)
    elif radioLinear:
        colorWheel("linear")
        ellipse(radPosX, 110, 10, 10)
    elif radioExponential:
        colorWheel("exponential")
        ellipse(radPosX, 140, 10, 10)




