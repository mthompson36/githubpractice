
#hard coded list
a =[1,5,5,6,8,22,33,698,55,56,45,78,99,100,21,509]
print(max(a))

print("***********************************************")


b = [4,5,6,2,33,32,11,23,2342,323,23,90,44,5667]
#set initial value of max to 0
max = 0
#for loop to index through each number in the list
for element in b:
	#compares the current index you are on if it's greater than the 'current max' which will change as you cycle through the loop
	if element > max:
		#if the current element is greater than the max, it will set the current element number as the new max.
		max = element
print(str(max) + " is the max number of your list")