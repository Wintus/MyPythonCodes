# Project:      (ZhangYiwuHomework06Sec01.py)
# Name:         Yiwu Zhang
# Date:         06/16/14
# Description:  This program will make four types of reports of proverty.

from graphics import *

class Guideline():
    #initialize
    def __init__(self, strState):
        self.state = strState
        if self.state == "AK":
            self.levels = (11630, 15610, 19590, 23570, 27550, 31530, 35510, 39490)
            self.additional = 3980
        elif self.state == "HI":
            self.levels = (10700, 14360, 18020, 21680, 25340, 29000, 32660, 36320)
            self.additional = 3660
        else:
            self.levels = (9310, 12490, 15670, 18850, 22030, 25210, 28390, 31570)
            self.additional = 3180
            
    def getLevel(self, intSize):
        #return the level of poverty by the side of family unit
        if intSize >= 1 and intSize <= 8:
            return self.levels[intSize - 1]
        elif intSize > 8:
            return self.levels[-1] + self.additional * (intSize - 8)

def isPoverty(family):
    # return Boolean
    guideline = Guideline(family[3])
    #if the income below the level
    return family[2] < guideline.getLevel(family[1])


def show(family):
    return "ID#: {}\tSize:{}\tIncome: {:,}\tState: {}"\
           .format(family[0], family[1], family[2], family[3])

def report(intMode, strReport, familyList):
    if strReport:
        report = open(strReport, mode='w', encoding='utf-8')
    if intMode == 1:
        for family in familyList:
            if isPoverty(family):
                report.write(show(family) + '\n')
    if intMode == 2:
        #initialize
        strReport = 'all the families that are above the average income\n\n'
        fltSum = 0
        for family in familyList:
            fltSum += family[2] #income
        fltAverageIncome = fltSum / len(familyList)
        for family in familyList:
            if family[2] >= fltAverageIncome:
                strReport += (show(family) + '\n')
        return strReport
    if intMode == 3:
        intFamilyNumber = 0
        for family in familyList:
            if isPoverty(family):
                intFamilyNumber += 1
        return intFamilyNumber / len(familyList) * 100
    if intMode == 4:
        for family in familyList:
            if isPoverty(family):
                report.write(show(family) + "\tStatus: Poverty" + '\n')
            else:
                report.write(show(family) + "\tStatus: Non Poverty" + '\n')
    #finished writing
    if strReport: report.close()


def importFile(strFilename):
    familyList = []
    aFile = open(strFilename)
    for line in aFile:
        familyList.append(line.split())
    #covert first 3 elements of lists into numbers
    for family in familyList:
        for i in range(3):
            family[i] = int(family[i])
    #finished the work 
    aFile.close()
    return familyList

class Textbox():
    #initialize
    def __init__(self, p1, p2, strText):
        self.p1 = p1
        self.p2 = p2
        self.box = Rectangle(p1, p2)
        self.text = Text(self.box.getCenter(), strText)

    def draw(self, window):
        self.box.draw(window)
        self.text.draw(window)

    def isClicked(self, point):
        intLeft = self.p1.getX()
        intRight = self.p2.getX()
        intDown = self.p1.getY()
        intUp = self.p2.getY()
        return (intLeft < point.getX() < intRight) \
               and (intDown < point.getY() < intUp)

def main():
    #initialize
    masterList = []
    imported = False
    #make a window
    win = GraphWin("poverty report", 600, 400)
    win.setCoords(0, 0, 6 + 2, 16)
    #initialize the list of the buttons
    listButtons = []
    labels = ("Import", "Report1", "Report2", "Report3", "Report4", "EXIT")
    for i in range(6):
        listButtons.append(Textbox(Point(1 + i, 1), Point(2 + i, 2),
                                   labels[i]))
        listButtons[i].draw(win)
    #output area textbox
    output = Textbox(Point(1, 3), Point(7, 15), "output area")
    output.draw(win)
    #inifiny loop to get mouse clicks
    while True:
        #get a mouse click
        clicked = win.getMouse()
        #exit button 
        if listButtons[5].isClicked(clicked):
            win.close()
            break #get out the loop
        #import button
        if listButtons[0].isClicked(clicked):
            #use importFile function to make a masterlist
            strFilename = "familySurveyData.txt"
            masterList = importFile(strFilename)
            output.text.setText("Imported")
            #recorde already clicked or not in a boolean
            imported = True
        #report1 button
        elif listButtons[1].isClicked(clicked) and imported:
            #make a report 1
            strReport1 = "Zhang_Yiwu_report01.txt"
            report(1, strReport1, masterList)
            output.text.setText("Report 1 was outputed")
        #report2 button
        elif listButtons[2].isClicked(clicked) and imported:
            output.text.setText((report(2, '', masterList)))
        #report3 button
        elif listButtons[3].isClicked(clicked) and imported:
            output.text.setText(
                "the percentage of families below the poverty level:\n{:0.2f}%"\
                .format(report(3, '', masterList)))
        #report4 button
        elif listButtons[4].isClicked(clicked) and imported:
            strReport4 = "Zhang_Yiwu_report04.txt"
            report(4, strReport4, masterList)
            output.text.setText("Report 4 was outputed")
        elif not imported:
            output.text.setText("you should import first")

main()
