#Compares values in 2 list and prints the matching values into one list
import random

def listcompare():
	a = [1,1,2,3,5,8,13,21,25,34,55,89]
	b = [1,2,3,4,5,6,7,8,9,10,11,12,13,25]

	samelist = []

	for element in a:
		if element in b:
			samelist.append(element)
	print(samelist)

listcompare()
print("**************************************************************")
#creates 2 random list and then compares and empties into new list

nmlist = []
for x in range(0,25):
	x = random.randint(1,10)
	nmlist.append(x)
print(nmlist)

nm2list = []
for b in range(0,25):
	b = random.randint(1,10)
	nm2list.append(b)
print(nm2list)

finallist = []
for element in nmlist:
	if element in nm2list:
		finallist.append(element)
print(finallist)