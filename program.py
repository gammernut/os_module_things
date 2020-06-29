import utill

import os

import datetime

utill.print_header(code_name='os module things')
# utill.new_new()

# print(dir(utill))  # lists all the dot things i can use ie utill.print_header()
# print(dir(os))  # lists all the dot things i can use ie os.path
#
# print(os.getcwd())
#
# # os.chdir('D:\\codeing\\projects')
#
# os.chdir('D:\\codeing\\projects\\fucking _with_file_IO_for_untitled')  # changes working dir to another dir
# # two \\ are being used because other wise it wont work
#
# print(os.getcwd())  # gets the current working directory / folder
# print(os.listdir())  # list all the sub-dir in the current working dir
# print(os.getcwd())
#
# os.mkdir('os_Demo_1')  # can only make one folder
# os.makedirs('os_Demo_2\\Demo_2_sub_folder')  # can make several folders nested
#
# print(os.listdir())
#
# os.rmdir('os_Demo_1')  # removes only the one dir just like os.mkdir but not
# os.removedirs('os_Demo_2\\Demo_2_sub_folder')  # removes all just like os.makedirs but not
#
# print(os.listdir())  # nothing to list i just deleted it
#
# os.mkdir('os_Demo_1')
# os.makedirs('os_Demo_2\\Demo_2_sub_folder')
#
# print(os.listdir())
#
# os.rename('os_Demo_1', 'os_rename_1')  # renames the thing in the first spot with the second
# os.rename('os_Demo_2', 'os_rename_2')

# os.chdir('D:\\codeing\\projects\\fucking _with_file_IO_for_untitled\\os_rename_1')
# print(os.listdir())
#
# print(os.stat('Demo.txt'))  # gives in about the thing ie Demo.txt
# print(os.stat('Demo.txt').st_size)  # size of file in bytes
# print(os.stat('Demo.txt').st_mtime)  # last mod time not very human readable
#
# mod_time = os.stat('Demo.txt').st_mtime
#
# print(datetime.date.fromtimestamp(mod_time))  # now you can read it

os.chdir('D:\\codeing\\projects\\fucking _with_file_IO_for_untitled')

print(os.getcwd())

# for dirpath, dirnames, filenames in os.walk('D:\\codeing\\projects'):
#     print('current path: ', dirpath)
#     print('Dir: ', dirnames)
#     print('files', filenames)
#     print()

