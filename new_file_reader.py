import logging


def right_name_reader():
    try:
        file = open("new_file.txt")
        for line in file:
            print(f"{line}", end="")
        file.close()
    except FileNotFoundError as e:
        print("that didn't work,man")
        logging.error(e)


def wrong_name_reader():
    try:
        file = open("is_this_new_file?.py")
        for line in file:
            print(f"{line}", end="")
        file.close()
    except FileNotFoundError as e:
        print("that didn't work,man")
        logging.error(e)


# right_name_reader()
# wrong_name_reader()
