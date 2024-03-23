import logging
import os


# def right_name_writer():
#     try:
#         with open("/Users/chris/pyprojects/PythonFundamentals.Exercises.Part8/new_file.txt", "a") as file:
#             file.write("hi!!!")
#             #for line in file:
#                 #print(f"{line}", end="")
#                  #file.writelines(["hey there"])
#     except FileNotFoundError as e:
#         print("that didn't work,man")
#         logging.error(e)



def name_writer(path,message):
    try:
        with open(path, "a") as file:
            file.write("\n"+message)
            #for line in file:
                #print(f"{line}", end="")
                 #file.writelines(["hey there"])
    except FileNotFoundError as e:
        print("that didn't work,man")
        logging.error(e)


# def wrong_name_reader():
#     try:
#         file = open("is_this_new_file?.py")
#         for line in file:
#             print(f"{line}", end="")
#         file.close()
#     except FileNotFoundError:
#




#right_name_reader()
# wrong_name_reader()


tree = os.listdir("/Users/chris/pyprojects/PythonFundamentals.Exercises.Part8/")

def path_lister():
    #holder for strings
    file_list = ""
    for item in tree:
        if os.path.isfile(item):
            file_list += f'./{item}\n'
           # print()
        else:
            for file in os.listdir(item):
                file_list += f'./{item}/{file}\n'
               # print(f'./{item}/{file}')
    return file_list


name_writer("/Users/chris/pyprojects/PythonFundamentals.Exercises.Part8/new_file.txt", path_lister())

#file_path_list =[os.listdir(child_dir) for child_dir in tree if os.path.isdir(child_dir)]

#print(file_path_list)