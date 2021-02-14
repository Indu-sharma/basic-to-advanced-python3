import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "python3-learning-indu",
    version = "1.0",
    author = "Indu Sharma",
    author_email = "indu.sharma.acharya@gmail.com",
    description = ("Learning Python with Indu"),
    license = "BSD",
    keywords = "Python3  Algorithms Advance Classes Python-tricks",
    url = "http://packages.python.org/python3-learning-indu",
    packages=['python3-learning-indu'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic ::Learning Python ",
        "License :: OSI Approved :: BSD License",
    ],
)
