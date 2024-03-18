import logging
import os

#from file_reader import
try:
    with open("/Users", 'r') as file:
        print(file)


except FileNotFoundError:
    print('Couldn\'t find the file!')
