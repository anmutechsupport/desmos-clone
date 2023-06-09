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
    # # Save the old x and y values
    # old_x = 0
    # old_y = (-1*a*math.sin(k*scaleFactor*(old_x-width/2-d))+c)*scaleFactor + height/2
    # for i in range(1, fs):  # Starting from 1, because 0 is used for old_x and old_y
    #     x = i*dx
    #     y = (-1*a*math.sin(k*scaleFactor*(x-width/2-d))+c)*scaleFactor + height/2
    #     line(old_x, old_y, x, y)  # Draw a line from the old point to the new point
    #     old_x, old_y = x, y  # Update the old values
    beginShape()
    x = 0
    y = (-1*a*math.sin(k*scaleFactor*(x-width/2-d))+c)*scaleFactor + height/2
    curveVertex(x, y)  # Additional vertex for smooth curve
    
    for i in range(fs):
        x = i*dx
        y = (-1*a*math.sin(k*scaleFactor*(x-width/2-d))+c)*scaleFactor + height/2
        curveVertex(x, y)
    
    x = (fs-1)*dx
    y = (-1*a*math.sin(k*scaleFactor*(x-width/2-d))+c)*scaleFactor + height/2
    curveVertex(x, y)  # Additional vertex for smooth curve
    endShape(OPEN)


