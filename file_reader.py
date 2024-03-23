import logging


# This function will attempt to open a file and process it.
# What could go wrong?
def reckless_file_reader(file_path: str) -> None:
        file = open(file_path)
        for line in file:
            print(f"{line}", end="")
        file.close()



# When an unhandled exception occurs, the application will be terminated.
# We can avoid this by wrapping the code in a try statement.
# This next function will show you what not to do.
# Seriously, NEVER do this. This is known as eating an exceptions.
# This anti-pattern will hide bugs in your code and cause endless headache.
def quick_way_to_get_fired(file_path: str) -> None:
    try:
        reckless_file_reader(file_path)
    except PermissionError:
        "cant access file"



# Once we know our code has the potential to raise exceptions, we can handle the exception properly like the code below.
# We can determine which exceptions are raised by
# looking at the documentation and/or source code for the apis we are interacting with.
def single_exception_handling_reader(file_path: str) -> None:
    try:
        reckless_file_reader(file_path)
    except FileNotFoundError as e:
        print("No such file or directory: 'file_that_does_not_exist.txt'")
        logging.error(e)




# We can handle as many different types of exceptions as we need to.
def multiple_exception_handling_reader(file_path: str) -> None:
    try:
        reckless_file_reader(file_path)
    except FileNotFoundError as e:
        logging.error(e)
        print("Could not find the file with the provided path.")
    except PermissionError as e:
        logging.error(e)
        print("Permission denied: 'locked_out_file.txt'")



# Sometimes we intend to handle different exceptions in the same way.
# If these errors share the same base class, we can simply catch the base class.
# FileNotFoundError and PermissionError share the same base class (OSError).
# In order to avoid having repetitive code we could simply provide an except clause matching the base class.
def base_class_exception_handling_reader(file_path: str) -> None:
    try:
        reckless_file_reader(file_path)
    except OSError as e:
        print("Error opening the file. Please ensure the file exists and has appropriate permissions.")
        logging.error(e)


# If we want to handle different exceptions in the same way but those exceptions don't share a base class,
# we can use a tuple to handle them in the same except clause.
def tuple_exception_handling_reader(file_path: str) -> None:
    try:
        reckless_file_reader(file_path)
    except (FileNotFoundError, PermissionError) as e:
        print("Error opening the file. Please ensure the file exists and has appropriate permissions.")
        logging.error(e)


# In order to make our code more robust, let's separate the responsibility of opening the file and processing the file.
def process_file(file) -> None:
    for line in file:
        print(line)


# This time we provide clauses for all of the known potential issues.
# The request to process the file is only issued if no exceptions occur.
# Regardless of what took place, at the end of the function, the resource (file) is closed.
def better_file_reader(file_path: str) -> None:
    file = None
    try:
        file = open(file_path)
    except OSError as e:
        print("Error opening the file. Please ensure the file exists and has appropriate permissions.")
        logging.error(e)
    else:
        process_file(file)
    finally:
        file.close() if file else logging.warning("No file resource available to close.")

