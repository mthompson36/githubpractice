from behave import *
from externalmodules.driversetup import close_driver
from externalmodules.staginglogin import staging_login
from externalmodules.vetsearch import search_veteran
from externalmodules.assertveteran import Veteran

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


@when('you assert on the proper url links')
def step_impl(context):
	page = Veteran(context.driver)
	page.search_veteran()

@then('assert veteran is in job title and description')
def step_impl(context):
	page = Veteran(context.driver)
	page.assert_veteran()
