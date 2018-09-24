"""
File I/O
Reading a file -> .read()
Reading a line by line -> .readline()
"""

my_file = open("firstfile.txt", 'r')
print(str(my_file.read()))
my_file.close()

print("read line by line ****************")

my_file = open("firstfile.txt", 'r')
print(str(my_file.readline()))
print(str(my_file.readline())) #calling it again will just read the second line, in which you could do a for loop. Say if you wanted to manipulate each line, but not all
my_file.close()