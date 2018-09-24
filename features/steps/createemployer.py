from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import uuid
import random
import time

from externalmodules.driversetup import close_driver
from externalmodules.staginglogin import staging_login

random_name = uuid.uuid4()



class EmployerCreation(object):

	def __init__(self):
		self.driver = staging_login()

	def post_a_job(self):
		wait = WebDriverWait(self.driver, 10)
		cookie = {'name' : 'disable_ab_tests', 'value' : '1', 'path': '/'}
		self.driver.add_cookie(cookie)
		postjob = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Post a Job"))).click()
		employeecount = Select(self.driver.find_element_by_name("org_type"))
		employeecount.select_by_index(2)
		submit = self.driver.find_element_by_name("submitted_uc_min").click()

	def employee_info(self):

		#pre determined values dictionary for employer account creation
		employee_dict = {'name': "jamestest", 'email_address':"jamest+{}".format(random_name) + "@ziprecruiter.co.uk",
						 'password':"Zip123zip123", 'phone_number':"555-555-5555",'org_name':"us test company0", 'zipcode':"90405"}

		#loop through each key and enter the defined values for each field
		for k,v in employee_dict.items():
			info = self.driver.find_element_by_name(k)
			info.send_keys(v)

		#Two dropdowns on employer sign up
		position = Select(self.driver.find_element_by_name("position"))
		position.select_by_index(1)
		plan = Select(self.driver.find_element_by_name("requested_plan"))
		plan.select_by_index(2)
		cont = self.driver.find_element_by_name("finish_create_account").click()

	def job_posting(self):

		time.sleep(3)
		#disabled a/b test for job description 250 words
		cookie = {'name' : 'disable_ab_tests', 'value' : '1', 'path': '/'}
		self.driver.add_cookie(cookie)

		jobdescription_dict = {'quizname':"us test job1", 'freeform_location':"Los Angeles,CA",
								'why_work_here_blurb':"Awesome CEO, great benefits", 'display_address':"123 Test Ave." }

		for k,v in jobdescription_dict.items():
			info = self.driver.find_element_by_name(k)
			info.send_keys(v)

		description = open("//Users/jamest/Desktop/jobdescription.txt", 'r')
		job_description = self.driver.find_element_by_class_name('')
		job_description.send_keys('test')
		time.sleep(4)







page = EmployerCreation()
page.post_a_job()
page.employee_info()
page.job_posting()



