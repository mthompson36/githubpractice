#This will ask for a string, then will tell you if it's a palindrome or not.
inputstring = input("Please enter a word: ")

if inputstring[::-1] == inputstring[0:]:
	print(str(inputstring) + " is a palindrome")
else:
	print(str(inputstring) + " is not a palindrome")