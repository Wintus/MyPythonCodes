'''Table in graphics'''

from graphics import *

class Exit(Exception): pass

def draw_all(canvas, *objects):
    for obj in objects:
        obj.draw(canvas)

def in_area(self, point):
    '''whether point is in the area of rectangle or not
    return Boolean'''
    left_end    = self.p1.getX()
    right_end   = self.p2.getX()
    top_end     = self.p1.getY()
    bottom_end  = self.p2.getY()
    return left_end < point.getX() < right_end \
           and top_end < point.getY() < bottom_end

Rectangle.in_area = in_area

class TextBox(Rectangle, Text):
    '''a textbox'''
    def __init__(self, point, width, height, text, bound='ALL'):
        self.point  = point
        self.width  = width
        self.height = height
        self.bound  = bound
        self.p1  = self.point.clone()
        self.p2  = self.point.clone()
        self.p2.move(width, height)
        self.box    = Rectangle(self.p1, self.p2)
        self.text   = Text(self.box.getCenter(), text)
        if bound:
            self.box.setOutline("black")
        else:
            self.box.setOutline('') # no lines

    def draw(self, graphwin):
        draw_all(graphwin, self.box, self.text)

    def setText(self, text):
        '''override the Text's'''
        self.text.setText(text)
