#This program will take your inputed number and check the list and return all numbers lower than and equal to inputed number in a new list.

numanswer = int(input("Please enter a number: "))

def newlist(numanswer):

	a = [1,1,2,3,5,8,13,21,34,55,89]
	new_list = []

	for element in a:
		if element <= numanswer:
			new_list.append(element)
	print(new_list)

newlist(numanswer)


"""for element in a:
	if element <= 5:
		new_list.append(element)
		print(new_list)
	else:
		quit()"""
