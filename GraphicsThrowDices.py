# Project:      Lab 8: Dice (MaemichiYuyaLab08Sec01.py)
# Name:         Yuya Maemichi
# Date:         05/30/14
# Description:  This program will displays the 5 side of a dice.

from graphics import *
import random
##from itertools import product

class Square(Rectangle):
    '''a square'''
    def __init__(self, center_point, size):
        self.center = center_point
        self.size   = size
        half = size / 2
        p1 = center_point.clone()
        p1._move(-half, -half)
        p2 = center_point.clone()
        p2._move(half, half)
        Rectangle.__init__(self, p1, p2)

    def getCenter(self):
        return self.center

    def getSize(self):
        return self.size
        
class Dice(Square, Dot):
    '''a dice object'''
    
##    pointss     = [[center_point.clone() for m in range(n - 1)] \
##                   for n in range(1, 7)]
    pointss     = []
    for n in range(6):
        points = []
        for m in range(n + 1):
            points.append(center_point.clone())
        pointss.append(points)
    # == [[Point], [Point, Point(], ... , [..., Point]]
    for i in range(1, 6): # topLeft & bottomRight of 2, 3, 4, 5, 6
        pointss[i][0].move(-space, -space)
        pointss[i][1].move(space, space)
    for i in range(3, 6): # bottomLeft & topRight of 4, 5, 6
        pointss[i][2].move(-space, space)
        pointss[i][3].move(space, -space)
    # the center two of 6
    pointss[5][4].move(-space, 0)
    pointss[5][5].move(space, 0)
##    print(list(map(lambda l: \
##                   list(map(lambda p: (p.getX(), p.getY()), l)), \
##                   pointss)))
    
    def __init__(self, center_point, size, number):
        self.number = number
        half    = size / 2
        space   = size / 4
        radius  = size / 10

        # make a white square base
        self.box = Square(center_point, size)
        self.box.setFill("white")

        # make dots
##        self.dots   = tuple(range(6))
        self.dots = []
##        for n in range(6):
        points = pointss[number]
        self.dots = [Dot(p, radius) for p in points]
##        self.dots.append(dots)
##        for ds in self.dots:
##            for d in ds:
##                c = d.getCenter()
##                print(c.x, c.y, d.getRadius(), end=", ")
##            print()

    def __call__(self, *n): # callable instance
        '''_ -> throw, n -> show n'''
        if not n: # [] == no argument
            self = self.clone(random.randint(1, 6))
        elif n[0]: # a number
            self = self.clone(int(n[0]))
        else:
            raise ValueError("Invalid argument")

    def clone(self, n=self.number):
        other = Dice(self.center, self.size, n)
        other.config = self.config.copy()
        return other

class Dot(Circle):
    '''a black dot'''
    def __init__(self, center_point, radius):
        Circle.__init__(self, center_point, radius)
        self.setFill("black")

def dice(intNumber, centerPoint, intSize, graphwin):
    '''create a dice with <intNumber> dots at <centerPoint> of <intSize> on <graphwin>'''
    intX = centerPoint.getX()
    intY = centerPoint.getY()
    intL = intSize // 2
    intS = intSize // 4
    intR = intSize // 10
    
    # create a white box
    box  = Rectangle(Point(intX - intL, intY - intL), \
                     Point(intX + intL, intY + intL))
    box.setFill("white")
    box.draw(graphwin)
    
    # initialize dots
    dot0, dot1, dot2, dot3, dot4, dot5 = tuple(range(6))
    dots = (dot0, dot1, dot2, dot3, dot4, dot5)
    
    # prepare the coordinates for 1 dot to 6 dots in each lines
    points  = (\
        (Point(intX, intY), ), \
        (Point(intX - intS, intY - intS), Point(intX + intS, intY + intS)), \
        (Point(intX, intY), \
             Point(intX - intS, intY - intS), Point(intX + intS, intY + intS)), \
        (Point(intX - intS, intY - intS), Point(intX + intS, intY - intS), \
             Point(intX + intS, intY + intS), Point(intX - intS, intY + intS)), \
        (Point(intX, intY), \
             Point(intX - intS, intY - intS), Point(intX + intS, intY - intS), \
             Point(intX + intS, intY + intS), Point(intX - intS, intY + intS)), \
        (Point(intX - intS, intY - intS), Point(intX + intS, intY - intS), \
             Point(intX - intS, intY), Point(intX + intS, intY), \
             Point(intX + intS, intY + intS), Point(intX - intS, intY + intS))\
        )
    
    # draw each dots by dot()
    for d, p in zip(dots, points[intNumber - 1]):
        # zip(): [1, 2, 3, 4] & [a, b, c] -> [(1, a), (2, b), (3, c)]
        # (omit the excess)
        d = dot(p, intR, graphwin)
        
    return box, dots # return a tuple
    

def dot(centerPoint, intSize, graphwin):
    '''create and draw a black dot at <centerPoint> of <intSize> on <graphwin>'''
    dot = Circle(centerPoint, intSize)
    dot.setFill("black")
    dot.draw(graphwin)
    return dot

def textbox(strText, centerPoint, intWidth, intHeight, graphwin):
    '''create a textbox with <strText> of <intWidth> & <intHeight> on <graphwin>'''
    intX = centerPoint.getX()
    intY = centerPoint.getY()
    intW = intWidth  // 2
    intH = intHeight // 2
    # make a box
    box  = Rectangle(Point(intX - intW, intY - intH), \
                     Point(intX + intW, intY + intH))
    box.setFill("white")
    # make a text
    text = Text(centerPoint, strText, )
    # draw the both
    box.draw(graphwin)
    text.draw(graphwin)
    return text, box

def inArea(rectangle, point):
    '''determine the clicked point is in the rectangular area or not'''
    pointX      = point.getX()
    pointY      = point.getY()
    leftEnd     = rectangle.getP1().getX()
    rightEnd    = rectangle.getP2().getX()
    topEnd      = rectangle.getP1().getY()
    bottomEnd   = rectangle.getP2().getY()
    return leftEnd < pointX < rightEnd \
           and topEnd < pointY < bottomEnd # return Boolean

def main():
    '''the main function'''
    # create window
    intWidth    = 400
    intHeight   = 300
    intSize     = 100
    win         = GraphWin("Dice", intWidth, intHeight)
    
    # draw Exit button
    textboxExit = textbox("EXIT", Point(intWidth * .9, intHeight * .9), \
                          80, 50, win) # (text, box)
    # draw Show button
    textboxClick = textbox("Click to\n show dices", \
                           Point(intWidth // 2, intHeight // 2 + intSize), \
                           100, 50, win) # (text, box)

##    # entry of the number of the dice
##    entry = Entry(Point(intWidth // 2, intHeight // 2 - intSize * .9), 3)
##    entry.setText('5')
##    entry.draw(win)
##
##    # and its tip
##    strText = "Enter the number of dots"
    strText = "Throw 3 dices"
    textboxNumber = textbox(strText, \
                            Point(intWidth // 2, intHeight // 2 - intSize * 1.2), \
                            200, 30, win) # (text, box)

    # infinity loop to get mouse click unless push exit button
    while True:
        clicked = win.getMouse()
##        textboxNumber[0].setText(strText) # textboxNumber = (text, box)
        if inArea(textboxClick[1], clicked):
            # draw a dice
##            intNumber = int(entry.getText())
##            if 1 <= intNumber <= 6:
                dice0 = dice(random.randint(1, 6), \
                             Point(intWidth // 4 * .8, intHeight // 2), \
                             intSize, win)
                dice1 = dice(random.randint(1, 6), \
                             Point(intWidth // 2, intHeight // 2), intSize, win)
                dice2 = dice(random.randint(1, 6), \
                             Point(intWidth *3.2 // 4, intHeight // 2), \
                             intSize, win)
##            else:
##                textboxNumber[0].setText("Invaild Input")
        elif inArea(textboxExit[1], clicked):
            break # jump out from the loop
     
    #finally close the window
    win.close()

##if __name__ == '__main__': #run only in a direct call
##    main()
