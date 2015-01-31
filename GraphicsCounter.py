'''Simple counter'''

from graphics import *

def main():
    '''main function'''
    width   = 400
    height  = 300
    maxSize = 36 - 5 + 1
    win = GraphWin("Counter", width, height)
    count = 0
    text = Text(Point(width / 2, height / 2), str(count))
    text.setSize(5 + count)
    text.draw(win)

    while True:
        if win.getMouse():
            count += 1
            text.setText(str(count))
            if 0 < count < maxSize:
                text.setSize(5 + count)

                
main()
