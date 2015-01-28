"""Dicision Sturcture (If Statement)"""

def grade(*args):
    """Get a score (100-point) form the imput, and return a letter grade

    90-100:A, 80-89:B, 70-79:C, 60-69:D"""

    #Get a score
    fltScore = float(input("Enter your score: "))

    strRepeat = "Your grade is"

    #Grade the score
    if 100 < fltScore:
        print("Invalid score.")
        return -1
    elif 90 <= fltScore: #in [90, 100]
        print(strRepeat, 'A.')
        return 0
    elif 80 <= fltScore: #in [80,90)
        print(strRepeat, 'B.')
        return 1
    elif 70 <= fltScore: #in [70,80)
        print(strRepeat, 'C.')
        return 2
    elif 60 <= fltScore: #in [60,70)
        print(strRepeat, 'D.')
        return 3
    elif 0 <= fltScore: #in [0, 60]
        print("No grade.")
        return 9
    else:
        print("Invalid score.")
        return -1

if __name__ == '__main__':
    grade()
