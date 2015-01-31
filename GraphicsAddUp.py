'''Add Up Graphics'''

from graphics import *

def textbox(text, centerP, width, height):
    '''make a textbox with a centered text'''
    centerX = centerP.getX()
    centerY = centerP.getY()
    box = Rectangle(Point(centerX - width / 2, centerY + height / 2), \
                    Point(centerX + width / 2, centerY - height / 2))
    in_text = Text(centerP, text)
    return box, in_text

def drawAll(graphlist, graphwin):
    '''use draw methods of graphlist to graphwin'''
    for g in graphlist:
        g.draw(graphwin)

def box_clicked(rectangle, graphwin, value):
    '''check click in a rectangle area

    return: value'''
    # get the area
    left_end    = rectangle.getP1().getX()
    right_end   = rectangle.getP2().getX()
    top_end     = rectangle.getP1().getY()
    bottom_end  = rectangle.getP2().getY()
    # wait for click
    point = graphwin.getMouse()
    if left_end < point.getX() < right_end and \
       bottom_end < point.getY() < top_end:
        # do only within the rectangle
        return value
    else:
        return None

def main():
    '''main function'''
    # settings
    intWidth  = 300
    intHeight = 200
    intBlank  =  20
    intX      = intWidth  / 4 # base position
    intY      = intHeight / 4
    listGraph = [] # the list of to draw
 
    # make title textbox "Add"
    win = GraphWin("Add Up", intWidth, intHeight)
    add_box, add_text = textbox("Add", Point(intWidth / 4, intHeight / 4), \
                                50, 30) # textbox "Add"
    listGraph.extend((add_box, add_text)) # add the tuple to the list
    
    # make entries and formula
    intY1 = intY + 30 + intBlank
    entry1 = Entry(Point(intX, intY1), 6)
    text_plus = Text(Point(intX + 20 + intBlank, intY1), '+')
    entry2 = Entry(Point(intX + 40 + intBlank * 2, intY1), 6)
    text_eq = Text(Point(intX + 60 + intBlank * 3, intY1), '=')
    
    listGraph.extend((entry1, text_plus, entry2, text_eq)) # add to the list

    # result box
    result_box, result_text = textbox('', Point(intX + 85 + intBlank * 4, \
                                                intY1), \
                                      60, 20)
    listGraph.extend((result_box, result_text)) # add them

    # exit box
    exit_box, exit_text = textbox("Quit", Point(intX + 85 + intBlank * 4, \
                                                intY1 + 30 + intBlank), \
                                  50, 30)
    listGraph.extend((exit_box, exit_text))

    # display
    drawAll(listGraph, win)

    # caluculate
    while True:
        if box_clicked(add_box, win, True): # calc the sum
            intNumber1  = int(entry1.getText())
            intNumber2  = int(entry2.getText())
            intSum      = intNumber1 + intNumber2
            result_text.setText(str(intSum))
        elif box_clicked(exit_box, win, True): # close the window
            break
            
    win.close()
    
main()
