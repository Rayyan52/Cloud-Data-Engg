# print("Hey cloud")
# print("Saylani class 1")
# print("Python Programming")
# print("PYTHON 4 EVERYONE")
# print("Python is easy to learn")
# print("Python is easy to learn")
# print(1+1)
# print("Hello rayyan and nabeedah")

# we are now doing file handling in python 

# with open('D:/task.txt', 'r') as file:
#     content = file.read()
#     print(content)

# with open('D:/task.txt', 'w') as file:
#     file.write("Hello World this is my first file handling in python" )
#     file.write("\n")
#     file.write("Python is easy to learn")

# f = open('D:/task.txt', 'r')
# f = f.readlines()
# print(len(f))

f = open('D:/task.txt', 'r')
f = f.read()
change = f.replace('()', '[]')

with open('D:/task.txt', 'w') as file:
    file.write(change)
    print(change)
