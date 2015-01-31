# Project:      Lab 8: Dice (MaemichiYuyaLab08Sec01.py)
# Name:         Yuya Maemichi
# Date:         05/30/14
# Description:  This program will displays the 5 side of a dice.

from graphics import *
import random

DEBUG = True

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
        self.number = number
        self.index  = self.number - 1
        half    = size / 2
        space   = size / 4
        radius  = size / 10

        # make a white square base
        self.box = Square(center_point, size)
        self.box.setFill("white")

        # make dots
        def pss(i):
            points = []
            nonlocal center_point, space
            for n in range(6):
                ps = []
                for m in range(n + 1):
                    ps.append(center_point.clone())
                points.append(ps)
            # == [[Point], [Point, Point], ... , [..., Point]]
            if i in range(1, 6):
                points[i][0].move(-space, -space)
                points[i][1].move(space, space)
            if i in range(3, 6):
                points[i][2].move(-space, space)
                points[i][3].move(space, -space)
            if i == 5:
                # the middle two of 6
                points[5][4].move(-space, 0)
                points[5][5].move(space, 0)
            return points[i]

        self.dots   = tuple(Dot(p, radius) for p in pss(self.index))

    def getNumber(self):
        return self.number

    def setNumber(self, n):
        '''n :: int'''
        if 1 <= n <= 6:
            self.number = n

    def draw(self, canvas):
        # draw box
        self.box.draw(canvas)
        # draw dots
        for d in self.dots:
            d.draw(canvas)

    def undraw(self):
        # undraw box
        self.box.undraw()
        # undraw dots
        for d in self.dots:
            d.undraw()

    def __call__(self, *n): # callable instance
        '''_ -> throw, n -> show n'''
        if not n: # [] == no argument
            self.setNumber(random.randint(1, 6))
        elif n[0]: # a number
            self.setNumber(int(n[0]))
        else:
            raise ValueError("Invalid argument")
        if DEBUG: print("Number:", self.getNumber())
        return self.clone()

    def clone(self):
        other = Dice(self.center, self.size, self.number)
##        other.config = self.config.copy()
        return other

class TextBox(Rectangle, Text):
    '''a textbox'''
    def __init__(self, center, text, width, height, color=""):
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
        self.box.setFill(color)

    def draw(self, canvas):
        self.box.draw(canvas)
        self.text.draw(canvas)

    def clone(self):
        other = TextBox(self, self.center, self.text, self.width, self.height)
##        other.cenfig = self.config.copy()
        return other

# extend the object methods
def redraw(self, win):
    self.undraw()
    self.draw(win)
    
def in_area(self, point):
    '''return Bool'''
    left_end    = self.p1.getX()
    right_end   = self.p2.getX()
    top_end     = self.p1.getY()
    bottom_end  = self.p2.getY()
    return left_end < point.getX() < right_end \
           and top_end < point.getY() < bottom_end

Rectangle.in_area       = in_area # add it as unbound method
GraphicsObject.redraw   = redraw  # as well

def draw_all(canvas, *sequance):
    for obj in sequance:
        obj.draw(canvas)


#run only in a direct call
if __name__ == '__main__':
    # create window
    intWidth    = 600
    intHeight   = 300
    intSize     = 100
    intMargin   =  20
    color       = "white"
    win         = GraphWin("Dice", intWidth, intHeight)
    
    # make Exit button
    textbox_exit = TextBox(Point(intWidth * .9, intHeight * .9), "EXIT", \
                           80, 50, color)
    # make Show button
    textbox_click = TextBox(Point(intWidth // 2, intHeight // 2 + intSize), \
                            "Click to throw\n all dices", 120, 60, color)
    # make tip
    strText = "Click each places to throw a dice"
    textbox_n = TextBox(Point(intWidth // 2, intHeight // 2 - intSize), \
                        strText, 300, 30, color)
    # show sum
    strSum = "Sum: "
    textbox_sum = TextBox(Point(intWidth * .1, intHeight * .9), \
                          strSum, 100, 50, color)
    # show the number of the thrown
    strThrown = "Thrown: "
    intThrown = 0
    textbox_thrown = TextBox(Point(intWidth * .3, intHeight * .9), \
                             strThrown + str(intThrown), 100, 50, color)  
    # prepare positions of 5 dices
    point   = Point(intWidth / 2, intHeight / 2)
    points  = tuple(p.clone() for p in (point, ) * 5)
    for p, n in zip(points, range(-2, 2 + 1)):
        p.move((intSize + intMargin) * n, 0)
    # make 5 rooms
    rooms = tuple(TextBox(p, "Dice {}".format(n + 1), *([intSize + 10] * 2)) \
                  for n, p in enumerate(points))
    # draw textboxes
    draw_all(win, textbox_exit, textbox_click, textbox_n, \
             textbox_sum, textbox_thrown, *rooms)

    # make 5 dices
    n = 0
    dices = tuple(Dice(p, intSize, n) for p in points)
    ds = dices
    num = [0] * 5
           
    # infinity loop to get mouse click unless push exit button
    try:
        while True:
            clicked = win.getMouse() # wait until clicked
            # check the throw button
            if textbox_click.in_area(clicked):
                # throw & draw all dices
                intThrown += 5
                ds = tuple(d() for d in dices)
                draw_all(win, *ds)
            # check the exit button
            elif textbox_exit.in_area(clicked):
                raise Exit("Exit button pushed") # jump out from the loop
            else:
                # check each rooms
                for i in range(5):
                    if rooms[i].box.in_area(clicked):
                        ds[i]().draw(win)
                        intThrown += 1
                        break
            # calc the sum of the dices
            if DEBUG: print("Dices:", tuple(d.getNumber() for d in ds))
            num = sum(d.getNumber() for d in ds)
            if DEBUG: print("Sum:", num)
            # refresh the text of the textbox
            textbox_sum.text.setText(strSum + str(num))
            textbox_thrown.text.setText(strThrown + str(intThrown))
    except Exit:
        print("Exit")
    finally:
        #finally close the window
        win.close()
