def setup():
    # Set the size of your sketch
    size(300,300)
    
    

    
def draw():
    # Starting with the largest ellipse, use a for loop to draw a bullseye with ellipses
    
    # Use an if statement and modulo to alternate the color of your rings
    for n in range (10):
        if n % 2 == 0:
            fill(200,40,140)
        else:
            fill(255,240,130)
        ellipse(150,150,300-n*30,300-n*30)
    
    
