

my_dict = {"bike":1300, "car":23000, "boat":75000}

"""for number in range(5):
	print(number, end=',')"""

d = {"name":"Eric", "age":26}

for key in d:
	print(d.items()) #list for each key and value in dictionary

for key in d:
	print(key, d[key]) #list each key and value in dictionary just once(not like above example)

for letter in "Eric":
	print(letter)

for key in my_dict:
	print(key, my_dict[key])

#List comprehensions
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print(evens_to_50)

even_squares = [x**2 for x in range(12) if x % 2 == 0]
print(even_squares)

cubes_by_four = [x**3 for x in range(11) if x % 4 ==0]  #not sure why x%4 w/o parenthesis doesn't work see example below
print(cubes_by_four)

cubes_by_four1 = [x**3 for x in range(1,11) if ((x**3) % 4 ==0)]
print(cubes_by_four1)

l = [x**2 for x in range(1,11)]
print(l[2:9:2])
