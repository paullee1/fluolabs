import fluo

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def setup():
    global angle
    size(400, 400)
    angle = 0
    background(0)
    
def draw(): 
    global angle 
    #background(0)
    stroke(random(255), random(255), random(255))
    strokeWeight(2)
    
    translate(width/2, height/2)
    fluo.showGrid()
    
    rotate(radians(angle))
    angle = angle + 1
    #line(-50, 0, 50, 0)
    #line(50, 0, 50, 100)
    #line(width/3, height/2, width * 2/3, height/2)
    moveForward(-50, 0, RIGHT)
    moveForward(50, 0, DOWN)
    moveForward(50, 100, LEFT)
    moveForward(-50, 100, UP)
    
def moveForward(x, y, dir):
    # move up
    if (dir == UP):
        line(x, y, x, y - 100)
    
    # move right
    elif(dir == RIGHT):
        line(x, y, x + 100, y)
    
    # move down
    elif (dir == DOWN):
        line(x, y, x, y + 100)
    
    # move left
    else:
        line(x, y, x - 100, y)
