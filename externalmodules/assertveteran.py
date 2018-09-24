from externalmodules.staginglogin import staging_login
from externalmodules.driversetup import close_driver


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import re	

VETERAN_SEARCH = "Search veteran jobs"
VETERAN_JOBS = "Search Jobs for Veterans"
JOB_TITLES = "just_job_title"
JOB_DESCRIPTIONS = "job_snippet"

class Veteran(object):

	def __init__(self, driver):
		self.driver = driver

	def search_veteran(self):

		wait = WebDriverWait(self.driver, 10)
		jobseeker = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "ZipCares"))).click()

		#assert on correct URL
		vet_search = self.driver.find_element_by_link_text(VETERAN_SEARCH).click()
		veteran_url = self.driver.current_url
		print(veteran_url.split("/"))
		assert "zipcares" and "veteran" in veteran_url, "Error:This is not the Veteran Search page"

		#assert on correct URL
		vet_jobs = self.driver.find_element_by_link_text(VETERAN_JOBS).click()
		veteran_jobs_url = self.driver.current_url
		print(veteran_jobs_url.split("/"))
		assert "search?search=veteran+friendly" in veteran_jobs_url,"Error:This is not the Veteran Job search page."

		#close job seeker signup popup
		veteran_popup = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "modal-close"))).click()

	def assert_veteran(self):
		
		job_title = self.driver.find_elements_by_class_name(JOB_TITLES)
		job_description = self.driver.find_elements_by_class_name(JOB_DESCRIPTIONS)

		for title in job_title:
			for description in job_description:
				if 'veteran' not in title.text.lower():
					assert 'veteran' in description.text.lower(), "Error: 'Veteran is not in job title or description: " +str(description.text)

