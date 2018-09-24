#This class will take a word you enter and return it capitalized
"""class getyourinput():

	#def __init__(self):
		#self.test = ""
	#function to get the string from user
	def get_string(self):
		self.test = raw_input("Please enter a word: ")
	#function to print string that was previously entered by user.
	def print_string(self):
		#prints the input variable that was entered in previous function
		print(self.test.upper())

#Initialize getyourinput class
a = getyourinput()
a.get_string()
a.print_string()"""



print("**********************************************************")
#This will take a sentence you enter and provide you with how many letters and digits are contained in it.
class GetLettersAndNumbers():

	def __init__(self):
		self.sentence = ""

	#function to get letter count.
	def get_letters(self):

		self.sentence = raw_input("Please enter a sentence with letters and numbers: ")
		letters = 0
		for x in self.sentence:
			if x.isalpha():
				letters = letters + 1
		print("The amount of letters in your sentence is: " + str(letters))
		
	#function to get digit/number count/calls same variable from previous function self.sentence to get count from same sentence entered by user. 
	def get_digits(self):
		digits = 0
		for y in self.sentence:
			if y.isdigit():
				digits = digits + 1
		print("The amount of digits in your sentence is: " + str(digits))


#initiate the getlettersandnumbers class
a = GetLettersAndNumbers()

a.get_digits()



print("*************************************************************")

#This function will multiply all the numbers in the list together from left to right.
"""randomlist = [5, 5, 5, 3, 4, 9, -4]

totalmult = 1
for x in randomlist:
	totalmult = totalmult * x
print(totalmult)"""








