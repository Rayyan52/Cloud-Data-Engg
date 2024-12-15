
# # we are now doing file handling in python 


# # writing and reading in python
with open('task.txt', 'r') as file:
    content = file.read()
    print(content)

# with open('D:/task.txt', 'w') as file:
    file.write("Hello World this is my first file handling in python" )
    file.write("\n")
    file.write("Python is easy to learn")


# # counting the number of lines in the file
f = open('task.txt', 'r')
f = f.readlines()
print(len(f))





# # replacing the brackets in the file
f = open('task.txt', 'r')
f = f.read()
change = f.replace(')', ']')
change = change.replace('(', '[')

with open('D:/task.txt', 'w') as file:
    file.write(change)
    print(change)


# using w+ mode to write and read the file
with open('test 2.txt', 'w+') as file:
    file.write("this is the file number 2" )
    file.seek(0)
    file.write("Python vs c++")
    content = file.read()
    print(content)

