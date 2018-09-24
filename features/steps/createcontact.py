from externalmodules.staginglogin import staging_login
from externalmodules.createjobseeker import create_contact

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


@when('user clicks the create contact link')
def step_impl(context):
	context.wait = WebDriverWait(context.driver, 10)
	cookie = {'name' : 'disable_ab_tests', 'value' : '1', 'path': '/'}
	context.driver.add_cookie(cookie)
	jobseeker = context.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Create Free Account"))).click()

@then('user fills in contact information')
def step_impl(context):
	create_contact(context.driver)