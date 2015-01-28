"""Dicision Sturcture (If Statement)"""

def grade(score):
    """Get a score (100-point), and return a letter grade.

    90-100:A, 80-89:B, 70-79:C, 60-69:D
    Return String"""

    def is_in_range(n, tpl_range):
        """Get a number and a tuple and check to be in the range.

    The range is lower-closed upper-open range: [a, b).
    Return Boolian"""
        return tpl_range[0] <= n < tpl_range[1]
    
    #Grade the score
    if 100 < score:
        print("Invalid score.")
        return '__ERROR__'
    elif is_in_range(score, (90, 100)) or score == 100: #in [90, 100]
        return 'A'
    elif is_in_range(score, (80, 90)): #in [80,90)
        return 'B'
    elif is_in_range(score, (70, 80)): #in [70,80)
        return 'C'
    elif is_in_range(score, (60, 70)): #in [60,70)
        return 'D'
    elif is_in_range(score, (0, 60)): #in [0, 60)
        return "No Grade"
    else:
        print("Invalid score.")
        return '__ERROR__'
    

if __name__ == '__main__':
    #Get a score
    fltScore = float(input("Enter your score: "))

    print("Your grade is {}.".format(grade(fltScore)))
