"""
This is used to find the absolute path. This is important for getting assets
"""
# Taken from https://stackoverflow.com/questions/51520/how-to-get-an-absolute-file-path-in-python (Lucas Azevedo)
from sys import argv
from os import path

ABSOLUTE_PATH = path.abspath(argv[0] + "/../..")