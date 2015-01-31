# Project:      Lab 8: Dice (MaemichiYuyaLab08Sec01.py)
# Name:         Yuya Maemichi
# Date:         05/30/14
# Description:  This program will displays the 5 side of a dice.

from graphics import *
import random

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
    points  = [\
        [Point(intX, intY)], \
        [Point(intX - intS, intY - intS), Point(intX + intS, intY + intS)], \
        [Point(intX, intY), \
             Point(intX - intS, intY - intS), Point(intX + intS, intY + intS)], \
        [Point(intX - intS, intY - intS), Point(intX + intS, intY - intS), \
             Point(intX + intS, intY + intS), Point(intX - intS, intY + intS)], \
        [Point(intX, intY), \
             Point(intX - intS, intY - intS), Point(intX + intS, intY - intS), \
             Point(intX + intS, intY + intS), Point(intX - intS, intY + intS)], \
        [Point(intX - intS, intY - intS), Point(intX + intS, intY - intS), \
             Point(intX - intS, intY), Point(intX + intS, intY), \
             Point(intX + intS, intY + intS), Point(intX - intS, intY + intS)]\
        ]
    
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
    textboxClick = textbox("Click to\n throw dices", \
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

if __name__ == '__main__': #run only in a direct call
    main()
