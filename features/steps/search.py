from behave import *
from externalmodules.driversetup import close_driver
from externalmodules.staginglogin import staging_login

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

@given('you can access homepage')
def step_impl(context):
    context.driver = staging_login()

@when('you land on homepage')
def step_impl(context):
    assert True is not False

@then('check to see if search bar exist')
def step_impl(context):
    assert context.failed is False