import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "cryptopals",
    version = "0.0.4",
    author = "Kaspar Hageman",
    author_email = "kasparhageman@gmail.com",
    description = ("The solutions to the Cryptopals challenges"),
    keywords = "cryptopals solution",
    url = "https://github.com/kdhageman/cryptopals",
    packages=['src']
)