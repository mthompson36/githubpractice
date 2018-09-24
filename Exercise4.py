#This program will take the number you input and return all numbers that are divisors of that number.

num = int(input("Please enter a number"))
divisorlist = []

for x in range(1, int(num + 1)):
	if int(num % x) == 0:
		divisorlist.append(x)
print(divisorlist)