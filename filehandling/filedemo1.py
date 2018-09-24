"""
File I/O
'w' -> Write-Only Mode
'r' -> Read-only mode
'r+' -> Read and Write Mode
'a' -> Append Mode
"""

my_list = ["first line", "second line", "third line"]

#my_file = open("//Users/jamest/Desktop/firstfile.txt", "w") 
my_file = open("firstfile.txt", "w")

for item in my_list:
	my_file.write(str(item) + "\n") #write function takes string argument, that's why put item as a string. Writes ONLY string arguments. \n writes items on new line as it goes through loop

my_file.close() #Always make sure you close the file. If not, it won't write properly