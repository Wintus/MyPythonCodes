"""Dicision Sturcture (If Statement)"""

def is_in_range(n, tpl_range, lower_closed=True, upper_closed=True):
    """Get a number and a 2-tuple and check to be in the range.

    The default range type is lower&upper-closed range: [a, b].
    Return Boolian."""
    def is_less_than_or_may_equal_to(a, b, equal=True):
        """Swichable evatuating "less than" | "less than or equal to"."""
        if equal:
            return a <= b
        else:
            return a < b

    #Evaluate lower <= n <= upper as default, and return the result (T|F).
    return is_less_than_or_may_equal_to(tpl_range[0], n, lower_closed)\
           and is_less_than_or_may_equal_to(n, tpl_range[1], upper_closed)
        # lower_closed : True -> a <= n | False -> a < n
        # upper_closed : True -> n <= b | False -> n < b
           
def grade(score):
    """Get a score (100-point), and return a letter grade.

    90-100:A, 80-89:B, 70-79:C, 60-69:D
    Return String."""

    #Grade the score.
    count = 0
    ranges = [(90,100),(80,90),(70,80),(60,70),(0,60)]
    grades = ['A','B','C','D','No Grade']
##    if score == 100: return 'A'
    for tpl_range in ranges:
        if is_in_range(score, tpl_range):
            return grades[count]
        else:
            count += 1
            
    raise ValueError('input number out of range')

if __name__ == '__main__':
    #Get a score.
    try:
        fltScore = float(input("Enter your score: "))
        print("Your grade is {}.".format(grade(fltScore)))
    except ValueError:
        print("Input correctly.")

##    scores = range(-10,120,5)
##    print('\n'.join((map(lambda tpl : ': '.join(map(str, tpl)),\
##                         list(zip(scores, map(grade, scores)))))))
