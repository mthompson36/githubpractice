string = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English."

print(string.lower())
print(string.count("it"))
print("**************************************************************************")

def list_count(list):
	total = 0
	for x in list:
		if len(x) >= 2:
			total = total+1
	return total

nlist = ["test", "cool", "it", "a","goodness","f", "5", "7", "love","joy"]

print(list_count(nlist))
print("***************************************************************************")

