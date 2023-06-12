import math 

fs = 100 # number of points to sample in frame 
scaleFactor = 20 # pixels/unit
h = 600
w = 600
dx = w/100 # pixels per adjacent sampling x-values x

def setup():
    size(h, w)  # Set the size of the window

# draw() code is run at many times per second (at the frameRate)
def draw():
    background(255)  # Set the background to white
    drawGrid()
    drawAxes()
    sin(10)
    quadratic()
    linear()
    exponential()

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
    noFill()  # Specify no fill
    x = 0
    y = (-1*a*math.sin(k*(1.0/scaleFactor*(x-width/2)-d))+c)*scaleFactor + height/2 # reflect across x-axis since x increments go from top to bottom of window, scale output by scaleFactor, vertically shift by height/2 to start from y=0
    curveVertex(x, y)  # Additional vertex for smooth curve
    
    for i in range(fs):
        x = i*dx
        # print(x)
        # print(k*((x-width/2.0)/scaleFactor-d)) # divide shifted x by scaleFactor since exactly scaleFactor number of pixels make up a unit on the graph 
        y = (-1*a*math.sin(k*(1.0/scaleFactor*(x-width/2)-d))+c)*scaleFactor + height/2 # input to sine should be a float value 
        # print(y)
        curveVertex(x, y)
    
    x = (fs-1)*dx
    y = (-1*a*math.sin(k*(1.0/scaleFactor*(x-width/2)-d))+c)*scaleFactor + height/2
    curveVertex(x, y)  # Additional vertex for smooth curve
    endShape()

def quadratic(a=1, b=0, c=0):
    beginShape()
    noFill()

    # Additional vertex for smooth curve at the start
    x = 0
    y = (-a*((1.0/scaleFactor*(x-width/2))**2)+b*(1.0/scaleFactor*(x-width/2))+c)*scaleFactor + height/2
    curveVertex(x, y)
    
    for i in range(fs):
        x = i*dx
        y = (-a*((1.0/scaleFactor*(x-width/2))**2)+b*(1.0/scaleFactor*(x-width/2))+c)*scaleFactor + height/2
        curveVertex(x, y)
    
    # Additional vertex for smooth curve at the end
    x = (fs-1)*dx
    y = (-a*((1.0/scaleFactor*(x-width/2))**2)+b*(1.0/scaleFactor*(x-width/2))+c)*scaleFactor + height/2
    curveVertex(x, y) 

    endShape()

def linear(m=1, b=0):
    beginShape()
    noFill()
    for i in range(fs):
        x = i*dx 
        y = (-m*(1.0/scaleFactor*(x-width/2))+b)*scaleFactor + height/2
        curveVertex(x, y)

    endShape()

def exponential(a=1, b=2, k=1, d=0, c=0):
    beginShape()
    noFill()  # Specify no fill

    # Additional vertex for smooth curve at the start
    x = 0
    y = (-a*b**(k*(1.0/scaleFactor*(x-width/2)-d))+c)*scaleFactor + height/2
    curveVertex(x, y)

    for i in range(fs):
        x = i*dx
        y = (-a*b**(k*(1.0/scaleFactor*(x-width/2)-d))+c)*scaleFactor + height/2
        curveVertex(x, y)
    
    # Additional vertex for smooth curve at the end
    x = (fs-1)*dx
    y = (-a*b**(k*(1.0/scaleFactor*(x-width/2)-d))+c)*scaleFactor + height/2
    curveVertex(x, y)  

    endShape()


