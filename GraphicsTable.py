'''Table in graphics'''

from graphics import *

def draw_all(canvas, *objects):
    for obj in objects:
        obj.draw(canvas)

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

class Cell(TextBox):
    '''a cell in table'''
        
class Column(Cell):
    '''a column consisted of cells'''
    def __init__(self, point, cell_width, cell_height, iterable):
        self.point = point
        number = len(iterable)
        self.width  = cell_width  * number
        self.height = cell_height * number
##        p1 = self.point.clone()
##        p2 = self.point.clone()
        self.box    = Recangle(p1, p2)
        if all(isinstance(item, Cell) for item in iterable):
            self.cells = iterable
        else:
            self.cells = make_serise(point, cell_width, cell_height, iterable)

    def make_serise(point, width, height, iterable):
        '''return a serise of Cells made by iterable'''

class Row(Column):
    '''a row consisted of columns'''
    def __init__(self, point, columns):
        self.point  = point
        self.columns= columns
        self.width  = sum(c.width for c in self.columns)
        self.height = self.columns[0].height
##        p1 = self.point.clone()
##        p2 = self.point.clone()
        p2.move(self.width, self.height)
        self.box    = Rectangle(p1, p2)

    def draw(self, graphwin):
        draw_all(graphwin, self.box, *self.cells)

class Table(Row):
    '''a table of rows'''

if __name__ == '__main__':
    intWidth    = 400
    intHeight   = 300
    intGridX    = 10
    intGridY    = 10
    win = GraphWin("Reports", intWidth, intHeight)
    win.setCoords(0, 0, intGridX, intGridY)

    textbox = TextBox(Point(1, 1), 2, 1, "Test")
    textbox.draw(win)
    
