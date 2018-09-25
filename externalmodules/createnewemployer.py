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

staging_login()

class EmployerCreation(object):

	def __init__(self, driver):
		self.driver = driver

	def post_a_job(self):
		wait = WebDriverWait(self.driver, 10)
		postjob = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Post a Job"))).click()
		time.sleep(3)

page = EmployerCreation()
page.post_a_job()