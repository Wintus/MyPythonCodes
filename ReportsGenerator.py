'''Reports Generator'''

from stdout import *

class States():
    '''US states and thier abbrebiations
    singleton'''
    def __init__(self):
        with open("states.txt", mode='r', encoding='utf-8') as a_file:
            states = {}
            for a_line in a_file:
                a_list = a_line.split()
                if a_list:
                    states[a_list[-1]] = ' '.join(a_list[:-1])
        self.states = states

    def __getitem__(self, abbrebiation='WA'):
        return self.states[abbrebiation.upper()].title()

    def is_state(self, name):
        a_name = name.upper()
        try:
            if self.states[a_name]:
                return True
        except KeyError:
            if any(a_name == state for abb, state in self.states.items()):
                return True
            else:
                return False
    
class Guideline():
    '''a guideline of a state'''
    def __init__(self, criterias, increment=0):
        self.list = criterias
        self.increment = increment

    def __getitem__(self, key):
        '''act like a dictionary / list'''
        # key = size of familiy unit
        if 1 <= key <= 8:
            return self.list[key - 1] # convert to index
        else:
            return self.increment * key

class Guidelines(Guideline):
    '''poverty guidelines of US
    singleton'''
    def __init__(self):
        self.states = States()
        self.Alaska = Guideline((11630, 15610, 19590, 23570, \
                                 27550, 31530, 35510, 39490), \
                                3980)
        self.Hawaii = Guideline((10700, 14360, 18020, 21680, \
                                 25340, 29000, 32660, 36320), \
                                3660)
        self.other = Guideline((9310, 12490, 15670, 18850, \
                                22030, 25210, 28390, 31570), \
                               3180)
        
    def __getitem__(self, state):
        if self.states[state] == 'Alaska':
            return self.Alaska
        elif self.states[state] == 'Hawaii':
            return self.Hawaii
        elif self.states.is_state(state):
            return self.other
        else:
            raise KeyError("Not a state")
    

class Family():
    '''imported data entry of families'''
    def __init__(self, id_number=-1, family_members_number=0, \
                 yearly_income=0, state_of_residence=''):
        # sample: 3489 4 4500 WA
        # a_family = Family(3489, 4, 4500, "WA")
        self.id     = int(id_number)
        self.number = int(family_members_number)
        self.income = int(yearly_income)
        self.state  = state_of_residence
        self.guidelines = Guidelines()

##    def get(self):
##        return self.id, self.number, self.income, self.state

    def is_poverty(self):
        guideline   = self.guidelines[self.state]
        if self.income < guideline[self.number]:
            return True
        else:
            return False

    def __repr__(self):
        return "ID#: {}\tMember: {}\tIncome: {:,}\tState: {}"\
               .format(self.id, self.number, self.income, self.state)
    
    def show_with_status(self, option=''):
        '''to write anything as option to add the status of poverty
    return: string'''
        if option:
            return str(self) + "\tStatus: {}"\
                   .format("Poverty" if self.is_poverty() else "Non Poverty")
        else:
            return str(self)
        

class Output():
    '''where to output: file / window'''
    def __init__(self, output_type='file', output_name='output.txt'):
        self.type = output_type # file / window
        self.name = output_name # filename / window object

    def getType(self):
        return self.type

    def getName(self):
        return self.name

    def is_file(self):
        return self.type == 'file'

    def is_window(self):
        return self.name == 'window'

class Report():
    '''report object of Families'''
    def __init__(self, families):
        self.families   = families
        
    def get_average(self):
        '''return the average level of the income'''
        return sum(family.income for family in self.families)\
                / len(self.families)

    def get_percentage(self):
        '''return the percentage of the families in poverty'''
        poverty_rate = sum(1 if family.is_poverty() else 0 \
                           for family in self.families)\
                        / len(self.families)
        return poverty_rate * 100
    
class ReportGenerator():
    '''make 4 different types of reports and output them
    singleton'''
    def __init__(self, data):
        '''data is list of Familiy instances'''
        self.data   = data
        self.report = Report(data)

    def generate(self, mode=1, output=Output('file', 'output.txt')):
        '''generate a Report object from given data and output'''
        if output.is_file:
            pass

class Window():
    '''the window to control and display reports
    singleton'''
##    from Table import *

def reporter(families, func, output):
    pass

if __name__ == '__main__':
    filenameIn  = "familySurveyData.txt"
    report1     = "Maemichi_Yuya_report01.txt"
    report4     = "Maemichi_Yuya_report04.txt"
    data_list   = []
    # open the file then store the data into the list
##    def import_file(filename):
    with open(filenameIn, encoding='utf-8') as file:
        for line in file:#.readlines():
            data = line.split()
##            print(data)
            data_list.append(Family(*data))
##    print(tuple(data.get() for data in data_list))
    # display on the shell
    def show(families):
        for family in families:
            print(family.show_with_status('SHOW'))
##    show(data_list)
    # write out the report1
    def the_poverties(families):
##        nonlocal report1 # not in the function! or must be in the main()
        report1 = "report1.txt"
        with open(report1, mode='w', encoding='utf-8') as report, \
             RedirectStdoutTo(report):
            for family in families:
                if family.is_poverty():
##                    report.write(family.show_with_status('SHOW') + '\n')
                    print(family.show_with_status('SHOW'))
    the_poverties(data_list)
    # display the report2
    def the_above(families, func):
        average = Report(families).get_average()
        for family in families:
            if family.income >= average:
##                func(str(family))
                func(family.show_with_status('FOO'))
    the_above(data_list, print)
    # display the report3
    print()
    def percentage(families):
        report3 = Report(families)
        print("In poverty: {:.1f}%".format(report3.get_percentage()))
    percentage(data_list)
    print()
    # write out the report4
    def with_status(families):
        report4 = "report4.txt"
        with open(report4, mode='w', encoding='utf-8') as report, \
             RedirectStdoutTo(report):
            for family in families:
##                report.write(family.show_with_status('SHOW') + '\n')
                print(family.show_with_status('SHOW'))
    with_status(data_list)
    # process finished
    print('finished')
