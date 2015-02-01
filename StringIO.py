'''use io.StringIO() with stdout.RedirectStdoutTo()'''

import io, stdout

def writeTwoLinesIntoAString():
    with io.StringIO() as output, stdout.RedirectStdoutTo(output):
        # this is equivalent with the below two lines
##    with io.StringIO() as output:
##        with stdout.RedirectStdoutTo(output):
        print("First line.")
        print("Second line.")
        contents = output.getvalue()
        return contents

if __name__ == '__main__':
    print(writeTwoLinesIntoAString(), end='')
