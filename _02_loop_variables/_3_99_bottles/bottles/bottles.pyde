def setup():
    size(400,600)
    
def draw():
    colPos = 10
    rowPos = 10
    for x in range(11):
        if 10-x>1:
            bottles = 10-x
            textSize(10)
            text(str(bottles) + " bottles of beer on the wall", colPos, rowPos)
            text(str(bottles) + " bottles of beer!", colPos, rowPos + 10)
            text("Take one down, pass it around", colPos, rowPos + 20)
            text(str(bottles-1) + " bottles of beer on the wall", colPos, rowPos + 30)
        elif 10-x == 1:
            textSize(10)
            text(str(1) + " bottle of beer on the wall", colPos, rowPos)
            text(str(1) + " bottle of beer!", colPos, rowPos + 10)
            text("Take one down, pass it around", colPos, rowPos + 20)
            text("No bottles of beer on the wall", colPos, rowPos + 30)
        else:
            textSize(10)
            text("No bottles of beer on the wall", colPos, rowPos)
            text("No bottles of beer!", colPos, rowPos + 10)
            text("Go to the store and buy some more", colPos, rowPos + 20)
            text(str(x) + " bottles of beer on the wall", colPos, rowPos + 30)
        rowPos+=50
