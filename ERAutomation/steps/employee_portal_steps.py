from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('The Employee is on the Employee Portal Page')
def open_employee_portal(context):
    context.driver.get("C:\\Users\\david\\Documents\\ExpenseReimbursementFrontend\\employeehomepage.html")


@given('The Employee is logged in as {username}')
def logged_in_as(context, username: str):
    context.driver.get("C:\\Users\\david\\Documents\\ExpenseReimbursementFrontend\\employeelogin.html")
    context.employee_login.username().send_keys(username)
    context.employee_login.password().send_keys("pass")
    context.employee_login.login_button().click()


@when('The Employee clicks on the submit new request button')
def new_request(context):
    context.employee_portal.submit_request_button().click()


@then('The Employee should be on the New request form page')
def verify_on_form_page(context):
    WebDriverWait(context.driver, 3).until(
        EC.title_is("New request form"))
    title = context.driver.title
    assert title == "New request form"


@when('The Employee clicks on the log out button')
def employee_logout(context):
    context.employee_portal.logout_button().click()


@then(u'The Employee should be on the Employee Login Page')
def verify_on_employee_login(context):
    WebDriverWait(context.driver, 3).until(
        EC.title_is("Employee Login"))
    title = context.driver.title
    assert title == "Employee Login"
