#This returns a new list of the even numbers from the original list.
a = [5,6,8,10,45,34,23,28,46,49,52,53]
b = []

for element in a:
	if element % 2 == 0:
		b.append(element)
print(b)

