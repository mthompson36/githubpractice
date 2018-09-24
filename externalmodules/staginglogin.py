from externalmodules.driversetup import return_driver #import driversetup module only for return driver function


"""
 This function opens zipstg.com by entering neccessary password for access
"""
def staging_login():


	#driver = driversetup.return_driver() # if you use 'import driversetup'
	driver = return_driver() # if you use 'from driversetup import return_driver, close_driver
	driver.get("http://www.zipstg.com")
	pwd = driver.find_element_by_name("devserver")
	pwd.send_keys("zipballgame")
	cookie = {'name' : 'closed_tos_update', 'value' : '1'}
	driver.add_cookie(cookie)
	submit = driver.find_element_by_class_name("btn-primary").click()
	return driver
