'''Table in graphics'''

from graphics import *

def draw_all(canvas, *objects):
    for obj in objects:
        obj.draw(canvas)

def redraw(self, graphwin):
    self.undraw()
    self.draw(graphwin)

GraphicsObject.redraw = redraw

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

def _resetWidth(self, width):
    '''reset the width to given width. require redraw'''

class TextBox(Rectangle, Text):
    '''a textbox'''
    def __init__(self, point, width, height, text, bound='ALL'):
        self.point  = point
        self.width  = width
        self.height = height
        self.bound  = bound
        p1  = self.point.clone()
        p2  = self.point.clone()
        p2.move(width, height)
        self.box    = Rectangle(p1, p2)
        self.text   = Text(self.box.getCenter(), text)
        if bound:
            self.box.setOutline("black")
        else:
            self.box.setOutline('') # no lines

    def draw(self, graphwin):
        draw_all(graphwin, self.box, self.text)

class Action():
    '''apply func to args'''
    def __init__(self, function, *arguments):
        self.func = function
        self.args = arguments

    def apply(self):
        return self.func(*self.args)

class Button(TextBox):
    '''add a feature to check clicks'''
    def __init__(self, point, width, height, text, action, bound='ALL'):
        self.action = action
        TextBox.__init__(self, point, width, height, text, bound='ALL')
        
    def is_clicked(self, point):
        if self.box.in_area(point):
            self.action.apply()
    
##class Cell(TextBox):
##    '''a cell in table'''
##        
##class Column(Cell):
##    '''a column consisted of cells'''
##    def __init__(self, point, cell_width, cell_height, iterable):
####        self.point = point
##        number = len(iterable)
##        self.width  = cell_width  * number
##        self.height = cell_height * number
####        p1 = self.point.clone()
####        p2 = self.point.clone()
##        self.box    = Recangle(p1, p2)
##        if all(isinstance(element, Cell) for element in iterable):
##            self.cells = iterable
##        else:
##            self.cells = make_serise(point, cell_width, cell_height, iterable)
##
##    def make_serise(point, width, height, iterable):
##        '''return a serise of Cells made by iterable'''
##
##class Row(Column, Cell):
##    '''a row consisted of columns'''
##    def __init__(self, point, columns):
####        self.point  = point
##        self.columns= columns
##        self.width  = sum(c.width for c in self.columns)
##        self.height = self.columns[0].height
####        p1 = self.point.clone()
####        p2 = self.point.clone()
##        p2.move(self.width, self.height)
##        self.box    = Rectangle(p1, p2)
##
##    def draw(self, graphwin):
##        draw_all(graphwin, self.box, *self.cells)
##
##class Table(Row):
##    '''a table of rows'''
##    def __init__(self, point, width, height, rows):
####        self.point  = point
##        self.width  = width
##        self.height = height
##        self.rows   = rows
##
##    def draw(self, graphwin):
##        draw_all(graphwin, self.box, *self.rows)

if __name__ == '__main__':
    intWidth    = 800
    intHeight   = 600
    intGridX    = 6 + 2
    intGridY    = 16
    intMargin   = .1
    win = GraphWin("Reports", intWidth, intHeight)
    win.setCoords(0, 0, intGridX, intGridY)

    actions = (Action(win.close, ), ) * 6
    buttons = tuple(Button(Point(index + 1 + intMargin, 1), \
                           (1 - intMargin * 2), 1, "Button" + str(index), \
                           Action(win.close, ))\
                    for index, action in zip(range(6), actions))
    draw_all(win, *buttons)
    
    clicked = win.getMouse()
    for button in buttons:
        button.is_clicked(clicked)
