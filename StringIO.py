'''use io.StringIO() with stdout.RedirectStdoutTo()'''

import io, stdout

if __name__ == '__main__':
    with io.StringIO() as output, stdout.RedirectStdoutTo(output):
        print("First line.")
        print("Second line.")
        contents = output.getvalue()

    print(contents)
