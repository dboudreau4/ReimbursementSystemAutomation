from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('The Manager is on the Manager Portal Page')
def open_manager_portal(context):
    context.driver.get("C:\\Users\\david\\Documents\\ExpenseReimbursementFrontend\\managerhomepage.html")


@given('The Manager is logged in as {username}')
def m_log_in(context, username: str):
    context.driver.get("C:\\Users\\david\\Documents\\ExpenseReimbursementFrontend\\managerlogin.html")
    context.manager_login.username().send_keys(username)
    context.manager_login.password().send_keys("pass")
    context.manager_login.login_button().click()


@given('The Manager has clicked on the View Statistics Button')
def view_stats_click(context):
    context.manager_portal.view_stats().click()


@when('The Manager clicks on the view button for a request')
def view_request(context):
    context.manager_portal.view_request_button().click()


@then('The Manager should be on the View Request Page')
def verify_on_request_page(context):
    WebDriverWait(context.driver, 3).until(
        EC.title_is("View Request"))
    title = context.driver.title
    assert title == "View Request"


@when('The Manager clicks on the log out button')
def manager_logout(context):
    context.manager_portal.logout_button().click()


@then('The Manager should be on the Manager Login Page')
def verify_on_manager_login(context):
    WebDriverWait(context.driver, 3).until(
        EC.title_is("Manager Login"))
    title = context.driver.title
    assert title == "Manager Login"
