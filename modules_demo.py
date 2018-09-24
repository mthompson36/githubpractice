"""
https://docs.python.org/3/library/
"""
import math
from math import sqrt
#import externalmodules.cars as cars #this is not the better way to do it
#from externalmodules import cars
from externalmodules.cars import info, carlocation

class ModulesDemo():

	def builtin_modules(self):
		print(int(math.sqrt(100))) #this format goes with 'import math' but if you don't import the whole module, use below
		print(sqrt(100)) #this format goes if you import one function from the built in math module

	def car_information(self):
		make = "BMW"
		model = "550i"
		location = "Los Angeles,CA"
		info(make,model) #dont need cars.info when current import is done, if other than you would use cars.info
		carlocation(location)

m = ModulesDemo()
#m.builtin_modules()
m.car_information()