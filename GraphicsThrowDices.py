# Project:      Lab 8: Dice (MaemichiYuyaLab08Sec01.py)
# Name:         Yuya Maemichi
# Date:         05/30/14
# Description:  This program will displays the 5 side of a dice.

from graphics import *
import random

class Exit(Exception): pass

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
        
class Dot(Circle):
    '''a black dot'''
    def __init__(self, center_point, radius):
        Circle.__init__(self, center_point, radius)
        self.setFill("black")

class Dice(Square, Dot):
    '''a dice object'''

    def __init__(self, center_point, size, number):
        self.center = center_point
        self.size   = size
        self.number = number - 1
        half    = size / 2
        space   = size / 4
        radius  = size / 10

        # make a white square base
        self.box = Square(center_point, size)
        self.box.setFill("white")

        # make dots
        pointss = []
        def pss():
            nonlocal pointss, center_point, space
            for n in range(6):
                points = []
                for m in range(n + 1):
                    points.append(center_point.clone())
                pointss.append(points)
            # == [[Point], [Point, Point], ... , [..., Point]]
            for i in range(1, 6): # topLeft & bottomRight of 2-6
                pointss[i][0].move(-space, -space)
                pointss[i][1].move(space, space)
            for i in range(3, 6): # bottomLeft & topRight of 4, 5, 6
                pointss[i][2].move(-space, space)
                pointss[i][3].move(space, -space)
            # the middle two of 6
            pointss[5][4].move(-space, 0)
            pointss[5][5].move(space, 0)
            return pointss

        self.dots   = []
        pointss     = pss()
        points      = pointss[self.number]
        self.pointss= pointss
        self.points = points
        self.dots   = [Dot(p, radius) for p in points]

    def getNumber(self):
        return self.number + 1

    def setNumber(self, n):
        '''n :: int'''
        if 1 <= n <= 6:
            self.number = n - 1

    def draw(self, canvas):
        # draw box
        self.box.draw(canvas)
        # draw dots
        for d in self.dots:
            d.draw(canvas)

    def __call__(self, *n): # callable instance
        '''_ -> throw, n -> show n'''
        if not n: # [] == no argument
            self.number = random.randint(1, 6)
            self = self.clone()
        elif n[0]: # a number
            self.setNumber(int(n[0]))
            self = self.clone()
        else:
            raise ValueError("Invalid argument")

    def clone(self):
        other = Dice(self.center, self.size, self.number)
##        other.config = self.config.copy()
        return other

class TextBox(Rectangle, Text):
    '''a textbox'''
    def __init__(self, center, text, width, height):
        self.center = center
        self.text   = text
        self.width  = width
        self.height = height
        x   = width  / 2
        y   = height / 2
        self.p1  = center.clone()
        self.p2  = center.clone()
        self.p1.move(-x, -y)
        self.p2.move(x, y)
        self.box    = Rectangle(self.p1, self.p2)
        self.text   = Text(center, text)
        self.box.setFill("white")

    def draw(self, canvas):
        self.box.draw(canvas)
        self.text.draw(canvas)

    def clone(self):
        other = TextBox(self, self.center, self.text, self.width, self.height)
##        other.cenfig = self.config.copy()
        return other

def in_area(self, point):
    '''return Bool'''
    left_end    = self.p1.getX()
    right_end   = self.p2.getX()
    top_end     = self.p1.getY()
    bottom_end  = self.p2.getY()
    return left_end < point.getX() < right_end \
           and top_end < point.getY() < bottom_end

Rectangle.in_area = in_area # add it as unbound method

def draw_all(canvas, *sequance):
    for obj in sequance:
        obj.draw(canvas)

##def dice(intNumber, centerPoint, intSize, graphwin):
##    '''create a dice with <intNumber> dots at <centerPoint> of <intSize> on <graphwin>'''
##    intX = centerPoint.getX()
##    intY = centerPoint.getY()
##    intL = intSize // 2
##    intS = intSize // 4
##    intR = intSize // 10
##    
##    # create a white box
##    box  = Rectangle(Point(intX - intL, intY - intL), \
##                     Point(intX + intL, intY + intL))
##    box.setFill("white")
##    box.draw(graphwin)
##    
##    # initialize dots
##    dot0, dot1, dot2, dot3, dot4, dot5 = tuple(range(6))
##    dots = (dot0, dot1, dot2, dot3, dot4, dot5)
##    
##    # prepare the coordinates for 1 dot to 6 dots in each lines
##    points  = (\
##        (Point(intX, intY), ), \
##        (Point(intX - intS, intY - intS), Point(intX + intS, intY + intS)), \
##        (Point(intX, intY), \
##             Point(intX - intS, intY - intS), Point(intX + intS, intY + intS)), \
##        (Point(intX - intS, intY - intS), Point(intX + intS, intY - intS), \
##             Point(intX + intS, intY + intS), Point(intX - intS, intY + intS)), \
##        (Point(intX, intY), \
##             Point(intX - intS, intY - intS), Point(intX + intS, intY - intS), \
##             Point(intX + intS, intY + intS), Point(intX - intS, intY + intS)), \
##        (Point(intX - intS, intY - intS), Point(intX + intS, intY - intS), \
##             Point(intX - intS, intY), Point(intX + intS, intY), \
##             Point(intX + intS, intY + intS), Point(intX - intS, intY + intS))\
##        )
##    
##    # draw each dots by dot()
##    for d, p in zip(dots, points[intNumber - 1]):
##        # zip(): [1, 2, 3, 4] & [a, b, c] -> [(1, a), (2, b), (3, c)]
##        # (omit the excess)
##        d = dot(p, intR, graphwin)
##        
##    return box, dots # return a tuple
##
##def dot(centerPoint, intSize, graphwin):
##    '''create and draw a black dot at <centerPoint> of <intSize> on <graphwin>'''
##    dot = Circle(centerPoint, intSize)
##    dot.setFill("black")
##    dot.draw(graphwin)
##    return dot
##
##def textbox(strText, centerPoint, intWidth, intHeight, graphwin):
##    '''create a textbox with <strText> of <intWidth> & <intHeight> on <graphwin>'''
##    intX = centerPoint.getX()
##    intY = centerPoint.getY()
##    intW = intWidth  // 2
##    intH = intHeight // 2
##    # make a box
##    box  = Rectangle(Point(intX - intW, intY - intH), \
##                     Point(intX + intW, intY + intH))
##    box.setFill("white")
##    # make a text
##    text = Text(centerPoint, strText, )
##    # draw the both
##    box.draw(graphwin)
##    text.draw(graphwin)
##    return text, box
##
##def inArea(rectangle, point):
##    '''determine the clicked point is in the rectangular area or not'''
##    pointX      = point.getX()
##    pointY      = point.getY()
##    leftEnd     = rectangle.getP1().getX()
##    rightEnd    = rectangle.getP2().getX()
##    topEnd      = rectangle.getP1().getY()
##    bottomEnd   = rectangle.getP2().getY()
##    return leftEnd < pointX < rightEnd \
##           and topEnd < pointY < bottomEnd # return Boolean

if __name__ == '__main__': #run only in a direct call
    # create window
    intWidth    = 400
    intHeight   = 300
    intSize     = 100
    win         = GraphWin("Dice", intWidth, intHeight)
    
    # make Exit button
##    textboxExit = textbox("EXIT", Point(intWidth * .9, intHeight * .9), \
##                          80, 50, win) # (text, box)
    textbox_exit = TextBox(Point(intWidth * .9, intHeight * .9), "EXIT", 80, 50)
    # make Show button
##    textboxClick = textbox("Click to\n show dices", \
##                           Point(intWidth // 2, intHeight // 2 + intSize), \
##                           100, 50, win) # (text, box)
    textbox_click = TextBox(Point(intWidth // 2, intHeight // 2 + intSize), \
                            "Click to\n throw dices", 100, 50)

    # make tip
    strText = "Throw 3 dices"
##    textboxNumber = textbox(strText, \
##                            Point(intWidth // 2, intHeight // 2 - intSize * 1.2), \
##                            200, 30, win) # (text, box)
    textbox_n = TextBox(Point(intWidth // 2, intHeight // 2 - intSize * 1.2), \
                        strText, 200, 30)

    draw_all(win, textbox_exit, textbox_click, textbox_n)

    # infinity loop to get mouse click unless push exit button
    try:
        while True:
            clicked = win.getMouse() # wait until clicked
    ##        if inArea(textboxClick[1], clicked):
            if textbox_click.in_area(clicked):
                # draw a dice
##                dice0 = dice(random.randint(1, 6), \
##                             Point(intWidth // 4 * .8, intHeight // 2), \
##                             intSize, win)
                dice0 = Dice(Point(intWidth / 4 * .8, intHeight / 2), intSize, \
                             random.randint(1, 6))
##                dice1 = dice(random.randint(1, 6), \
##                             Point(intWidth // 2, intHeight // 2), intSize, win)
                dice1 = Dice(Point(intWidth / 2, intHeight / 2), intSize, \
                             random.randint(1, 6))
##                dice2 = dice(random.randint(1, 6), \
##                             Point(intWidth // 4 * 3.2, intHeight // 2), \
##                             intSize, win)
                dice2 = Dice(Point(intWidth / 4 * 3.2, intHeight / 2), intSize, \
                             random.randint(1, 6))
                draw_all(win, dice0, dice1, dice2)
    ##        elif inArea(textboxExit[1], clicked):
            elif textbox_exit.in_area(clicked):
                raise Exit("Exit button pushed") # jump out from the loop
            else:
                pass
    finally:
        #finally close the window
        win.close()

##    # test
##    win = GraphWin("TEST", 400, 300)
##    textbox_exit = TextBox(Point(200, 70), "A Dice", 60, 20)
##    dice = Dice(Point(200, 150), 100, 5)
##    draw_all(win, textbox_exit, dice)
##    win.getMouse()
##    dice0 = dice.clone()
##    dice0(2)
##    print(dice0.getNumber())
##    dice0.draw(win)
