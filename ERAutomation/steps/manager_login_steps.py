from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('The Manager is on the Manager Login Page')
def open_manager_login(context):
    context.driver.get("C:\\Users\\david\\Documents\\ExpenseReimbursementFrontend\\managerlogin.html")


@when('The Manager types {username} into the username bar')
def type_m_username(context, username: str):
    context.manager_login.username().send_keys(username)


@when('The Manager types {password} into the password bar')
def type_m_password(context, password: str):
    context.manager_login.password().send_keys(password)


@when('The Manager clicks the login button')
def m_login(context):
    context.manager_login.login_button().click()


@then('The page title should be {title}')
def verify_on_manager_page(context, title: str):
    WebDriverWait(context.driver, 3).until(
        EC.title_is(title))
    assert context.driver.title == title
