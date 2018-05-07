import sys

"""With statements provides the context manager support in Python. With helps Built\n 
in open method for File handle to close the file when there is any error while file i/o in progress"""

with open(sys.argv[0]) as FH:
    lines_code = 0
    for line in FH:
        lines_code = lines_code + 1
print("Total Lines of codes : {}".format(lines_code))

# The above is ideally equavalent:

try:
    lines_code = 0
    FH = open(sys.argv[0])
    for line in FH:
        lines_code = lines_code + 1
finally:
    FH.close()
    print("Total Lines of codes: {}".format(lines_code))


# The Custom Implementation of Open in file open would look like:

class OpenFile:
    """My custom context manager"""

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'r')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


with OpenFile(sys.argv[0]) as FH:
    lines = FH.readlines()
    print("Total Lines of codes: {}".format(len(lines)))

# However, we dont need to override enter, exit methods for custom context manager simulation. We can just use the
# contextmanager lib.

from contextlib import contextmanager


@contextmanager
def OpenFile(name):
    try:
        f = open(name)
        yield f
    finally:
        f.close()


with OpenFile(sys.argv[0]) as f:
    lines = f.readlines()
    print("Total Lines of codes: {}".format(len(lines)))
