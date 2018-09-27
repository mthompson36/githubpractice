from externalmodules.driversetup import close_driver
from externalmodules.staginglogin import staging_login
from externalmodules.createnewemployer import EmployerCreation


@when('user clicks the post a job link')
def step_impl(context):
	emp = EmployerCreation(context.driver)
	emp.post_a_job()

@then('user fills in employer information')
def step_impl(context):
	emp = EmployerCreation(context.driver)
	emp.employee_info()