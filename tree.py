import logging
import os

#from file_reader import

print(os.path.abspath('file_reader.py'))
def right_name_reader():
    try:
        file = open("new_file.txt")
        for line in file:
            print(f"{line}", end="")
        file.close()
    except FileNotFoundError as e:
        print("that didn't work,man")
        logging.error(e)





'''
try:
    with open("/Users", 'r') as file:
        print(file)


except FileNotFoundError:
    print('Couldn\'t find the file!')
'''