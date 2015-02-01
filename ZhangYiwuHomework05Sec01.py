# Project:      Throw dice(ZhangYiwuHomework05Sec01.py)
# Name:         Yiwu Zhang
# Date:         06/03/14
# Description:  This program will let user throw five dices

from graphics import *
from random import randint 

def textbox(center, text, width, height, win):
    #calculate the p1, p2 from the center, width, height
    p1 = Point(center.getX() - width/2, center.getY() - height/2)
    p2 = Point(center.getX() + width/2, center.getY() + height/2)
    #make a retangle
    box = Rectangle(p1, p2)
    box.draw(win)
    #make a text
    text = Text(center, text)
    text.draw(win)
    return text, box

def dice(intNumber, center, intSize, win):
    #build a dice object
    #make a square(rectangle)
    #calculate the p1, p2 from the center point and size
    p1 = Point(center.getX() - intSize/2, center.getY() - intSize/2)
    p2 = Point(center.getX() + intSize/2, center.getY() + intSize/2)
    box = Rectangle(p1, p2)
    box.draw(win)
    box.setFill("white")
    #draw five dots
    intSpace = intSize / 4 
    intRadius = intSize / 10
    for center in calcPoints(center, intSpace, intNumber):
        dot(center, intRadius, win)

def calcPoints(center, intSpace, intNumber):
    #calcPoints function
    listPoints = []
    if intNumber in range(1, 5 + 1):
        listPoints.append(center.clone())
    if intNumber in range(2, 6 + 1):
        listPoints.append(Point(center.getX() - intSpace, \
                                center.getY() - intSpace))
        listPoints.append(Point(center.getX() + intSpace, \
                                center.getY() + intSpace))
    if intNumber in range(4, 6 + 1):
         listPoints.append(Point(center.getX() + intSpace, \
                                 center.getY() - intSpace))
         listPoints.append(Point(center.getX() - intSpace, \
                                 center.getY() + intSpace))
    if intNumber == 6:
        listPoints.append(Point(center.getX() - intSpace, center.getY()))
        listPoints.append(Point(center.getX() + intSpace, center.getY()))
    # return a list of dots
    return listPoints
    
def dot(center, radius, win):
    #creat a dot
    dot0 = Circle(center, radius)
    dot0.draw(win)
    dot0.setFill("black")

def isClicked(rectangle, clicked):
    p1 = rectangle.getP1()
    p2 = rectangle.getP2()
    withinX = p1.getX() < clicked.getX() < p2.getX()
    withinY = p1.getY() < clicked.getY() < p2.getY()
    #return Boolean
    return withinX and withinY
    
def main():
    # make a window
    win = GraphWin("dice", 600, 300)
    #5 coordinates for each boxes
    point1 = Point(80, 150)
    point2 = Point(190, 150)
    point3 = Point(300,150)
    point4 = Point(410, 150)
    point5 = Point(520, 150)
    points = (point1, point2, point3, point4, point5)

    squares = list(range(5))

    # make a exit button
    exitButton = textbox(Point(540, 270), "EXIT", 80, 50, win) # (text, box)
    # make a text
    Text(Point(135, 250), "dice total").draw(win)
    # show the total
    intSum = 0
    listSum = [0] * 5
    textSum = Text(Point(135, 275), str(intSum))
    textSum.draw(win)

    # draw dices
    for i in range(5):
        p = points[i]
        squares[i] = textbox(p, "Dice {}".format(i) , 90, 90, win)
##        dice(randint(1, 6), p, 80, win)

    # catch mouse clicks
    while True:
        clicked = win.getMouse()
        if isClicked(exitButton[1], clicked):
            win.close()
        for i in range(5):
##        for atextbox in squares:
            box = squares[i][1]
            if isClicked(box, clicked):
                intRandom = randint(1, 6)
                print(intRandom)
                listSum[i] = intRandom
                dice(intRandom, box.getCenter(), 80, win) # SEVERE BUG
                print(intRandom)
##        textSum.undraw()
        intSum = sum(listSum)
        textSum.setText(str(intSum))
main()
