webster = {"Aardvark": "A star of a popular children's cartoon show.", "Baa":"The sound a goat makes", "Carpet":"Goes on the floor", "Dab":"A small amount"}

for key in webster:
	print (key)
	print (webster[key])
print("****************************************************")
	#how many times a certain string,int,etc appears in a list

def test(x):

	total = 0
	for item in x:
		if item == "test":
			total = total +1
	return total

newlist = ["test", "dog", "test"]
print(test(newlist))
print("******************************************************")

price = {"banana":4,"apple":2,"orange":1.5,"pear":3}
stock = {"banana":6,"apple":0,"orange":32,"pear":15}

for x in price:
	print(x)
	print("price: %s" %price[x])
	print("stock: %s" %stock[x])
print("*******************************************************")

def compute_bill(food):

	total = 0
	for item in food:
		total = total + food[item]
	return total

print(compute_bill(stock))
print("********************************************************")

def compute_bill_case(food):

	total =0
	for item in food:
		if stock[item] >0:
			total = total + food[item]
			stock[item] = stock[item] - 1
	return total
	return stock[item]

print(compute_bill_case(price))	





