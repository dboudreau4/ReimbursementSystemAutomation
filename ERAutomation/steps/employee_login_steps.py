from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('The Employee is on the Employee Login Page')
def open_employee_login_to_portal(context):
    context.driver.get("C:\\Users\\david\\Documents\\ExpenseReimbursementFrontend\\employeelogin.html")


@when('The Employee types {username} into the username bar')
def type_in_username(context, username: str):
    context.employee_login.username().send_keys(username)


@when('The Employee types {password} into the password bar')
def type_in_password(context, password: str):
    context.employee_login.password().send_keys(password)


@when('The Employee clicks the login button')
def login(context):
    context.employee_login.login_button().click()


@then('The title should be {title}')
def verify_on_employee_page(context, title: str):
    WebDriverWait(context.driver, 3).until(
        EC.title_is(title))
    assert context.driver.title == title
