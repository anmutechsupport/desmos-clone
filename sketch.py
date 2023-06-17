import math 

# Set the resolution of the graph i.e. sampling rate 
fs = 100 

# Set the scaling factor for the graph. This is used to scale the size of the drawn functions.
scaleFactor = 20 

# Set the height and width for the canvas
h = 800
w = 800

# Calculate the width of each segment. It's the total width divided by the number of segments.
dx = w/fs 

# Initialize the position of the sliders at the start. There are four sliders and all start from position 50.
sliderX = [50, 50, 50, 50]

# Initialize the adjustment values for the sliders. These values will be used to adjust the parameters of the function.
adjustment = [0, 0, 0, 0]

# Initialize the labels for the sliders. Each slider corresponds to a parameter of the function: "a", "k", "d", "c".
sliderLabels = ["a", "k", "d", "c"]

# Initialize boolean variables for the radio buttons corresponding to each function: sin, quadratic, linear, exponential. 
# At the start, all are set to False. 
radioSin, radioQuadratic, radioLinear, radioExponential = False, False, False, False

# Set the X position of the radio buttons
radPosX = 600

# Initialize a boolean variable to decide whether to show sliders or not. It's initially set to True.
showSliders = True

# Define a function to dynamically change colors of the functions being drawn based on the function type.
# The 'funcName' parameter is the name of the function, and the 'prop' parameter determines whether it's for filling color or stroke color.
def colorWheel(funcName, prop="fill"): 
    # If 'prop' is "fill", then we're setting the fill color
    if prop == "fill":
        # If function is 'sin', set fill color to red
        if funcName == "sin":
            fill(255, 0, 0)
        # If function is 'quadratic', set fill color to green
        if funcName == "quadratic":
            fill(0, 255, 0)
        # If function is 'linear', set fill color to blue
        if funcName == "linear":
            fill(3, 61, 255)
        # If function is 'exponential', set fill color to purple
        if funcName == "exponential":
            fill(107, 3, 252)
    # If 'prop' is "stroke", then we're setting the stroke color
    if prop == "stroke":
        # If function is 'sin', set stroke color to red
        if funcName == "sin":
            stroke(255, 0, 0)
        # If function is 'quadratic', set stroke color to green
        if funcName == "quadratic":
            stroke(0, 255, 0)
        # If function is 'linear', set stroke color to blue
        if funcName == "linear":
            stroke(3, 61, 255)
        # If function is 'exponential', set stroke color to purple
        if funcName == "exponential":
            stroke(107, 3, 252)

# Define the 'setup' function, which is called once when the program starts
def setup():
    # Declare global variables that will be modified inside this function
    global radioSin, radioQuadratic, radioLinear, radioExponential, showSliders
    
    # Set the size of the canvas using the global 'h' and 'w' variables
    size(h, w)  

    # Set initial radio button states. Initially, the 'Sin' button is active and sliders are visible.
    radioSin = True
    showSliders = True

    # Initialize the sliders' positions and their corresponding adjustment values.
    # Each slider's x position is spaced out by 100 units and their adjustment values are normalized between 0.0 and 1.0.
    for i in range(4):
        sliderX[i] += i * 100
        adjustment[i] = 1.0 * (sliderX[i] - 50) / (350 - 50) # [0.0, 1.0] initialization, uses formula for normalizing values between 0 and 1, z = (x-min)/(max-min)


# Define the 'draw' function, which is called continuously by Processing
def draw():
    # Declare global variables that will be modified or used inside this function
    global radioSin, radioQuadratic, radioLinear, radioExponential
    global sliderX, adjustment

    # Set the background color to white
    background(255)

    # Call the functions to draw the grid and the axes on the canvas
    drawGrid()
    drawAxes()

    # Get the current value of the sliders and scale the adjustment to a range of [-10, 10]
    a = adjustment[0]*20 - 10  # scale adjustment to [-10, 10]
    k = adjustment[1]*20 - 10
    d = adjustment[2]*20 - 10
    c = adjustment[3]*20 - 10

    # Draw the corresponding graph based on which radio button is selected
    # Each function (sin, quadratic, linear, exponential) takes four parameters (a, k, d, c)
    if radioSin:
        sin(a, k, d, c)
    elif radioQuadratic:
        quadratic(a, k, d, c)
    elif radioLinear:
        linear(a, k, d, c)
    elif radioExponential:
        exponential(a, k, d, c)

    # Draw the radio buttons and sliders on top of everything else
    drawRadioButtons()
      
    # Check if the sliders are supposed to be visible, if so, draw them
    if showSliders:
        drawSliders()  # draw sliders last so they appear on top of the functions

# Define a function that's called whenever the mouse is clicked
def mouseClicked():
    # Declare the global variables that will be used or modified in this function
    global radioSin, radioQuadratic, radioLinear, radioExponential, showSliders
    global sliderX, adjustment

    # Check if the mouse was clicked on any of the sliders by comparing the mouse's x and y coordinates to each slider's position
    for i in range(4):
        if mouseX >= 50 and mouseX <= 350 and mouseY >= 40 + i * 50 and mouseY <= 60 + i * 50:
            # If so, move the clicked slider to the mouse's x position and update its corresponding adjustment value
            sliderX[i] = mouseX
            adjustment[i] = 1.0 * (sliderX[i] - 50) / (350 - 50)  # Adjustment values are always between 0 and 1

    # The radius of the radio buttons
    r = 10  
    
    # Check if a radio button was clicked by measuring the distance from the mouse to the button's position
    # If a button is clicked, set its corresponding variable to True and others to False
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

    # Check if the button to show or hide sliders was clicked by measuring the distance from the mouse to the button's position
    if dist(mouseX, mouseY, radPosX, 170) < r:  
        # If so, toggle the state of showSliders
        showSliders = not showSliders  

# Define a function that's called whenever the mouse is dragged
def mouseDragged():
    # Declare the global variables that will be used or modified in this function
    global sliderX, adjustment

    # Check if the mouse is being dragged on any of the sliders by comparing the mouse's x and y coordinates to each slider's position
    for i in range(4):
        if mouseX >= 50 and mouseX <= 350 and mouseY >= 40 + i * 50 and mouseY <= 60 + i * 50:
            # If so, move the dragged slider to the mouse's x position and update its corresponding adjustment value
            sliderX[i] = mouseX
            adjustment[i] = 1.0 * (sliderX[i] - 50) / (350 - 50)

# Define a function to draw the sliders
def drawSliders():
    global sliderX, sliderLabels

    # Draw the enclosing box for the sliders
    fill(255, 255, 255, 150)  # Set a semi-transparent white fill
    rectMode(CORNER)  # Switch the drawing mode to CORNER
    rect(30, 20, 400, 210)  # Draw a rectangle to enclose the sliders

    strokeWeight(3)  # Set the stroke weight for the sliders
    stroke(0)  # Set the stroke color to black

    # Draw the sliders
    for i in range(4):
        fill(100)  # Set the fill color to gray
        # Draw the line of the slider
        line(50, 50 + i * 50, 350, 50 + i * 50)
        # Draw the ends of the slider line
        line(50, 40 + i * 50, 50, 60 + i * 50)
        line(350, 40 + i * 50, 350, 60 + i * 50)
        rectMode(CENTER)  # Switch the drawing mode to CENTER for the sliders
        rect(sliderX[i], 50 + i * 50, 10, 30)  # Draw the slider handle
        fill(0)  # Set the fill color to black
        # Draw the slider label and value
        text(sliderLabels[i] + ": " + str(round(adjustment[i]*20 - 10, 1)), 360, 53 + i * 50)
        noFill()  # Disable filling geometry

# Define a function to draw the grid
def drawGrid():
    stroke(200)  # Set the grid line color to light gray
    # Draw vertical grid lines
    for i in range(0, width, scaleFactor):
        line(i, 0, i, height)
    # Draw horizontal grid lines
    for i in range(0, height, scaleFactor):
        line(0, i, width, i)

# Define a function to draw the axes
def drawAxes():
    stroke(0)  # Set the axes color to black
    strokeWeight(2)  # Set the axes thickness
    # Draw the x-axis
    line(0, height / 2, width, height / 2)
    # Draw the y-axis
    line(width / 2, 0, width / 2, height)

# Function for plotting sine curve
def sin(a=1, k=1, d=0, c=0):
    beginShape()  # Start a new shape
    colorWheel("sin", "stroke")  # Set stroke color using colorWheel function
    noFill()  # Specify no fill on the area under the curve

    x = 0  # Initialize x
    # Calculate y, scale x and y to fit in window, reflect y because processing's y increments from top to bottom of the window
    y = (-1*a*math.sin(k*(1.0/scaleFactor*(x-width/2)-d))-c)*scaleFactor + height/2
    curveVertex(x, y)  # Add a vertex to the shape at (x, y) for a smooth start

    for i in range(fs):  # Loop over sampling rate
        x = i*dx  # Scale x to fit in window
        y = (-1*a*math.sin(k*(1.0/scaleFactor*(x-width/2)-d))-c)*scaleFactor + height/2  # Recalculate y for new x
        curveVertex(x, y)  # Add vertex to shape at new (x, y)

    x = (fs-1)*dx  # Calculate final x value
    y = (-1*a*math.sin(k*(1.0/scaleFactor*(x-width/2)-d))-c)*scaleFactor + height/2  # Calculate final y value
    curveVertex(x, y)  # Add a vertex to the shape for a smooth end
    endShape()  # Finish the shape

# Function for plotting quadratic curve
def quadratic(a=1, k=1, d=0, c=0):
    colorWheel("quadratic", "stroke")  # Set stroke color using colorWheel function
    beginShape()  # Start a new shape
    noFill()  # Specify no fill on the area under the curve

    x = 0  # Initialize x
    # Calculate y, scale x and y to fit in window, reflect y because processing's y increments from top to bottom of the window
    y = (-a*k*(1.0/scaleFactor*(x-width/2)-d)**2-c)*scaleFactor + height/2 
    curveVertex(x, y)  # Add a vertex to the shape at (x, y) for a smooth start

    for i in range(fs):  # Loop over sampling rate
        x = i*dx  # Scale x to fit in window
        y = (-a*k*(1.0/scaleFactor*(x-width/2)-d)**2-c)*scaleFactor + height/2  # Recalculate y for new x
        curveVertex(x, y)  # Add vertex to shape at new (x, y)

    x = (fs-1)*dx  # Calculate final x value
    y = (-a*k*(1.0/scaleFactor*(x-width/2)-d)**2-c)*scaleFactor + height/2  # Calculate final y value
    curveVertex(x, y)  # Add a vertex to the shape for a smooth end

    endShape()  # Finish the shape


# Function for plotting a linear curve
def linear(a, k, d, c):
    beginShape()  # Start a new shape
    colorWheel("linear", "stroke")  # Set stroke color using colorWheel function
    noFill()  # Specify no fill for the shape
    for i in range(fs):  # Loop over sampling rate
        x = i*dx  # Scale x to fit in window
        y = (-a*k*(1.0/scaleFactor*(x-width/2)-d)-c) * scaleFactor + height/2  # Calculate y, scale x and y to fit in window, reflect y because processing's y increments from top to bottom of the window
        curveVertex(x, y)  # Add vertex to shape at new (x, y)
    endShape()  # Finish the shape

# Function for plotting an exponential curve
def exponential(a=1, k=1, d=0, c=0):
    beginShape()  # Start a new shape
    colorWheel("exponential", "stroke")  # Set stroke color using colorWheel function
    noFill()  # Specify no fill for the shape

    x = 0  # Initialize x
    # Calculate y, scale x and y to fit in window, reflect y because processing's y increments from top to bottom of the window
    y = (-a*2**(k*(1.0/scaleFactor*(x-width/2)-d))-c)*scaleFactor + height/2 
    if y > height: y = height  # If y exceeds the window height, set it to height
    if y < 0: y = 0  # If y falls below 0, set it to 0
    curveVertex(x, y)  # Add a vertex to the shape at (x, y) for a smooth start

    for i in range(fs):  # Loop over sampling rate
        x = i*dx  # Scale x to fit in window
        y = (-a*2**(k*(1.0/scaleFactor*(x-width/2)-d))-c)*scaleFactor + height/2  # Recalculate y for new x
        if y > height: y = height  # If y exceeds the window height, set it to height
        if y < 0: y = 0  # If y falls below 0, set it to 0
        curveVertex(x, y)  # Add vertex to shape at new (x, y)

    x = (fs-1)*dx  # Calculate final x value
    y = (-a*2**(k*(1.0/scaleFactor*(x-width/2)-d))-c)*scaleFactor + height/2  # Calculate final y value
    if y > height: y = height  # If y exceeds the window height, set it to height
    if y < 0: y = 0  # If y falls below 0, set it to 0
    curveVertex(x, y)  # Add a vertex to the shape for a smooth end

    endShape()  # Finish the shape

def drawRadioButtons():
    global radPosX, showSliders  # Access global variables

    # Draw the box first so it's underneath the radio buttons
    fill(255, 255, 255, 150)  # Set fill color to semi-transparent white
    rectMode(CORNER)  # Switch to CORNER mode, meaning (x,y) will be the coordinates of the upper-left corner
    rect(radPosX-30, 20, 200, 170)  # Draw a rectangle at (x,y) with width and height 200 and 170 respectively relative to the radio button x-positions

    # Draw the radio buttons
    fill(200)  # Set fill color
    stroke(0)  # Set stroke color
    # Draw outer circles (radio buttons) for each function
    ellipse(radPosX, 50, 20, 20)  # sin
    ellipse(radPosX, 80, 20, 20)  # quadratic
    ellipse(radPosX, 110, 20, 20)  # linear
    ellipse(radPosX, 140, 20, 20)  # exponential

    # Draw labels for the radio buttons
    textSize(16)  # Set text size
    # Use the colorWheel function to match the label color to the function
    colorWheel("sin")  
    text("sin", radPosX+50, 50)
    colorWheel("quadratic")
    text("quadratic", radPosX+50, 80)
    colorWheel("linear")
    text("linear", radPosX+50, 110)
    colorWheel("exponential")
    text("exponential", radPosX+50, 140)

    # Draw the selected radio button
    if radioSin:
        colorWheel("sin")  # Match the fill color to the function
        ellipse(radPosX, 50, 10, 10)  # Draw a smaller ellipse within the sin button to show it's selected
    elif radioQuadratic:
        colorWheel("quadratic")  
        ellipse(radPosX, 80, 10, 10)  # Same for the quadratic button
    elif radioLinear:
        colorWheel("linear")
        ellipse(radPosX, 110, 10, 10)  # And the linear button
    elif radioExponential:
        colorWheel("exponential")
        ellipse(radPosX, 140, 10, 10)  # And the exponential button

    # Draw the showSliders button
    fill(200)
    stroke(0)
    ellipse(radPosX, 170, 20, 20)  # sliders toggle
    textSize(16)
    fill(0)
    text("Show Sliders", radPosX+50, 175)
    if showSliders:  # If showSliders is True
        fill(0)
        ellipse(radPosX, 170, 10, 10)  # Draw a smaller ellipse within the button to show it's selected




