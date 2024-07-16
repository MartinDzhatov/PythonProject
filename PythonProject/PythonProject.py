#-------------------------------------------------------------------------------
# Course Work
# Martin Dzhatov
# 2023682
#-------------------------------------------------------------------------------


from PythonProject.graphics import *
import sys


def main():
    while True:
        patchworkSize = input("Enter patchwork size: ")
        if checkPatchwork(patchworkSize):
            break
    while True:
        colour1 = input("Enter first colour: ")
        colour2 = input("Enter second colour: ")
        colour3 = input("Enter third colour: ")
        if checkColour(colour1,colour2,colour3):
            break
    win = GraphWin("",int(patchworkSize)*100,int(patchworkSize)*100)
    drawDesgin(int(patchworkSize),win,0,0,colour1,colour2,colour3)

def drawDesgin(patchworkSize,win,tLCornerX,tLCornerY,colour1,colour2,colour3):
    #"i" is for keeping track of the row the program is on
    i=0
    #1-3Pattern are variables which track where the patterns should be drawn
    firstPattern = patchworkSize
    secondPattern = 0
    thirdPattern = patchworkSize-1
    while i<patchworkSize//2:
        for j in range(0,firstPattern):
            drawFinalDesgin(win,tLCornerX+100*(j+i),tLCornerY+100*i,colour1)
        i+=1
        firstPattern-=2
        secondPattern +=1
        for h in range (0,secondPattern):
            drawPenDesgin(win,tLCornerX+100*h,tLCornerY+100*i,colour2)

        for g in range(0,secondPattern):
            drawPenDesgin(win,tLCornerX+100*(thirdPattern+g),tLCornerY+100*i,colour3)
        thirdPattern-=1
    k = i
    thirdPattern+=2
    while i<=patchworkSize:

        for j in range(0,firstPattern):
            drawFinalDesgin(win,tLCornerX+100*(j+k),tLCornerY+100*i,colour1)
        i+=1
        firstPattern+=2
        k-=1
        secondPattern -=1

        for h in range (0,secondPattern):
            drawPenDesgin(win,tLCornerX+100*h,tLCornerY+100*i,colour2)

        for g in range(0,secondPattern):
            drawPenDesgin(win,tLCornerX+100*(thirdPattern+g),tLCornerY+100*i,colour3)
        thirdPattern+=1

#both checks are functions which verify if the user input is valid
def checkPatchwork(patchworkSize):
    validPatchwork = ["5", "7"]

    if patchworkSize in validPatchwork:
        patchworkSize=int(patchworkSize)
        return True
    else:
        print("Patch work can only be 5 or 7")
        return False

def checkColour(colour1,colour2,colour3):
    validColour = ["red", "green", "blue", "magenta", "orange", "cyan"]

    if colour1 in validColour and colour2 in validColour and colour3 in validColour:
        if colour1 == colour2 == colour3:
            print("Only two colours can be repeated")
            return False
        else:
            return True
    else:
        print("Valid colours are: red, green, blue, magenta, orange, cyan")
        return False

#drawing the Final desgin
def drawFinalDesgin(win,tLCornerX,tLCornerY,colour):
    for r in range(1,6):
        if r%2==1:
            finalEvenLine(win,tLCornerX,tLCornerY+(r-1)*20,colour)
        else:
            finalEvenLine(win,tLCornerX,tLCornerY+(r-1)*20,"white")


def finalEvenLine(win,tLCornerX,tLCornerY,colour):
    radius = 10
    center = Point(tLCornerX+radius,tLCornerY+radius)
    for i in range(0,5):
        drawCircle(win, center, radius, colour)
        center.x += 20

def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)

#drawing the Penultimate desgin
def drawPenDesgin(win,tLCornerX,tLCornerY,colour):
    for r in range(1,6):
        if r%2==1:
            penEvenLine(win,tLCornerX,tLCornerY+(r-1)*20,colour)
        else:
            penOddLine(win,tLCornerX,tLCornerY+(r-1)*20,colour)


def penEvenLine(win,tLCornerX,tLCornerY,colour):
    radius = 10
    lineX = tLCornerX
    center = Point(lineX+radius,tLCornerY+radius)
    drawTwoTriangles(win,lineX,tLCornerY,colour)
    center.x += 20
    drawCircle(win, center, radius, colour)
    center.x+=20
    lineX += 40
    drawTwoTriangles(win,lineX,tLCornerY,colour)
    center.x += 20
    drawCircle(win, center, radius, colour)
    center.x+=20
    lineX += 40
    drawTwoTriangles(win,lineX,tLCornerY,colour)

def penOddLine(win,tLCornerX,tLCornerY,colour):
    radius = 10
    lineX = tLCornerX
    center = Point(lineX+radius,tLCornerY+radius)
    drawCircle(win, center, radius, colour)
    lineX += 20
    drawTwoTrianglesFR(win,lineX,tLCornerY,colour)
    center.x += 40
    drawCircle(win, center, radius, colour)
    lineX += 40
    drawTwoTrianglesFR(win,lineX,tLCornerY,colour)
    center.x += 40
    drawCircle(win, center, radius, colour)

    #This two triangles are facing down
def drawTwoTriangles(win,tLCornerX,tLCornerY,colour):
    for i in range(2):
        triangle = Polygon(Point(tLCornerX,tLCornerY), Point(tLCornerX+20,tLCornerY), Point(tLCornerX+10,tLCornerY+10))
        triangle.draw(win)
        triangle.setFill(colour)
        tLCornerY += 10

    #FR = facing right
def drawTwoTrianglesFR(win,tLCornerX,tLCornerY,colour):
    for i in range(2):
        triangle = Polygon(Point(tLCornerX,tLCornerY), Point(tLCornerX,tLCornerY+20), Point(tLCornerX+10,tLCornerY+10))
        triangle.draw(win)
        triangle.setFill(colour)
        tLCornerX += 10

main()
input("Enter any key to quit.")
sys.exit() 











