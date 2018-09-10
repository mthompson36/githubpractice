#This will ask for name and age and tell you when you'll be 100. Using raw_input instead of 'input' cuz python 2 uses raw_input. Can run python3 exercise1.py with 'input'
year = 2018
name = raw_input("What is your name?")
print("Your name is: " + str(name))
age = int(raw_input("How old are you?"))
print("Your age is: " +str(age))
yearsto100 = int((100 - age) + year)
print("You will be 100 in the year: " + str(yearsto100))