from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import uuid
import time
import random

from externalmodules.driversetup import close_driver
from externalmodules.staginglogin import staging_login
 
random_name = uuid.uuid4()


#funcion to create new job seeker account from /contact/create page.
def create_contact(driver):

	name_dict = {'name':"jamest047",
		 'email_address':"jamest+{}".format(random_name) + "@ziprecruiter.com", 
		 'search':"Sales", 'location':"Los Angeles,CA", 
		 'resume':"//Users/jamest/Desktop/resume/resumetemplate1.rtf"}

	#for loop	 
	for k,v in name_dict.items():
		info = driver.find_element_by_name(k) #
		info.send_keys(v)
	submit = driver.find_element_by_name("submit").click()
	driver = close_driver(driver)


#driversetup.close_driver(driver) # if you use 'import driversetup'"""