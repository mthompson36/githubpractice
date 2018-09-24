from selenium import webdriver


def return_driver():
    driver = webdriver.Chrome()
    return driver

def close_driver(driver):
    driver.close()