from externalmodules.staginglogin import staging_login
from externalmodules.driversetup import close_driver


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import re	

VETERAN_SEARCH = "Search veteran jobs"
VETERAN_JOBS = "Search Jobs for Veterans"

def search_veteran(driver):

	wait = WebDriverWait(driver, 10)
	jobseeker = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "ZipCares"))).click()

	#assert on correct URL
	vet_search = driver.find_element_by_link_text(VETERAN_SEARCH).click()
	veteran_url = driver.current_url
	print(veteran_url.split("/"))
	assert "zipcares" and "veteran" in veteran_url, "Error:This is not the Veteran Search page"

	#assert on correct URL
	vet_jobs = driver.find_element_by_link_text(VETERAN_JOBS).click()
	veteran_jobs_url = driver.current_url
	print(veteran_jobs_url.split("/"))
	assert "search?search=veteran+friendly" in veteran_jobs_url,"Error:This is not the Veteran Job search page."

	#close job seeker signup popup
	veteran_popup = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "modal-close"))).click()
