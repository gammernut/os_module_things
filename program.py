import utill

import os

import datetime

# utill.print_header(code_name='os module things')
# utill.new_new()
#
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
#
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
#
# os.chdir('C:\\Users\\gamme\\Desktop')
#
# print(os.getcwd())
#
# for dirpath, dirnames, filenames in os.walk('D:\\codeing\\projects'):
#     print('current path: ', dirpath)
#     print('Dir: ', dirnames)
#     print('files', filenames)
#     print()
#
# print(os.environ.get('USERPROFILE'))
#
# file_path = os.path.join(os.environ.get('USERPROFILE'), 'test.txt')  # USERPROFILE instead of home makes it work
# print(file_path)
#
# with open(file_path, 'w') as f:
#     f.write()
#
# os.chdir('D:\\codeing\\projects\\fucking _with_file_IO_for_untitled')
# print(os.path.isdir('D:\\fsdf'))   # prints false since there is no fsdf folder
# print(os.path.isfile('D:\\fsdf'))   # prints false since there is no fsdf file
# print(os.path.splitext('D:\\tmp\\test.txt'))   # splits the file type off ie.
# #  ('D:\\tmp\\test', '.txt')
#
# print(dir(os.path))  # prints all the things you an do
#
#
# os.chdir('D:\\codeing\\projects\\fucking _with_file_IO_for_untitled')
# print(os.listdir())
# os.makedirs('test_folder')   # can make several folders nested
# # os.rename()  # renames the thing in the first spot with the second
# os.rmdir()  # removes only the one dir just like os.mkdir but not
# os.removedirs()  # removes all just like os.makedirs but not
# os.chdir('D:\\codeing\\projects\\fucking _with_file_IO_for_untitled\\test_folder')
# print(os.listdir())
#
# #  thires a better method but you can do this
#
# f = open('crap.txt', 'r')
# print(f.name) # prints name of file
# print(f.mode) # prints the read state ie r w r+ read write and both
# f.close()

#
# os.chdir('D:\\codeing\\projects\\fucking _with_file_IO_for_untitled\\test_folder')
# print(os.listdir())
#
# with open('crap.txt', 'r') as f:
#
#     f_contents = f.read()
#     print(f_contents, end='')


# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# student_info('math', 'art', name='john', age=22)

# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# courses = ['Math', 'Art']
# info = {'name': 'john', 'age': 22}
# student_info(*courses, **info)

# os.chdir('D:\\codeing\\projects\\fucking _with_file_IO_for_untitled\\test_folder')
# print(os.listdir())
#
# with open('crap.txt', 'r') as f:
#     size_to_read = 10
#     f_contents = f.read(size_to_read)
#     while len(f_contents) > 0:
#         print(f_contents, end='*')
#         f_contents = f.read(size_to_read)

# os.chdir('D:\\codeing\\projects\\fucking _with_file_IO_for_untitled\\test_folder')
# print(os.listdir())
#
# with open('crap.txt', 'r') as f:
#
#     for line in f:
#         print(line, end='')

# os.chdir('D:\\codeing\\projects\\fucking _with_file_IO_for_untitled\\test_folder')
# print(os.listdir())
#
# with open('crap.txt', 'r') as f:
#
#     size_to_read = 10
#
#     f_contents = f.read(size_to_read)
#     print(f_contents, end='')
#     f.seek(0)
#     f_contents = f.read(size_to_read)
#     print(f_contents)
# while len(f_contents) > 0:
#     print(f_contents, end='*')
#     f_contents = f.read(size_to_read)

# os.chdir('D:\\codeing\\projects\\fucking _with_file_IO_for_untitled\\test_folder')
# print(os.listdir())
#
# with open('also_crap.txt', 'w') as f:
#     f.write('Test')

# os.chdir('D:\\codeing\\projects\\fucking _with_file_IO_for_untitled\\test_folder')
# print(os.listdir())
#
# with open('shit_pic.jpg', 'rb') as rf:  # must add the b ie 'rb'
#     #  means biany makes work with other file types
#     with open('copy_shit_pic.jpg', 'wb') as wf:  # must add the b ie 'wb'
#         #  means biany makes work with other file types
#         for line in rf:
#             wf.write(line)

os.chdir('D:\\codeing\\projects\\fucking _with_file_IO_for_untitled\\test_folder')
print(os.listdir())

with open('shit_pic.jpg', 'rb') as rf:
    with open('copy_shit_pic.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
