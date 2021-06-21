from behave import given, when, then
from selenium.webdriver.support.ui import Select


@given('The Manager is on the View Request page')
def open_view_request(context):
    context.driver.get("C:\\Users\\david\\Documents\\ExpenseReimbursementFrontend\\viewrequest.html")


@given('The Manager has clicked the view request button')
def view_click(context):
    context.manager_portal.view_request_button().click()


@when('The Manager selects {status} from the status selector')
def select_status(context, status: str):
    sel: Select = context.manager_form.select()
    sel.select_by_value(status)


@when('The Manager types {manager_id} into the reviewed by box')
def manager_input(context, manager_id: str):
    context.manager_form.manager_id().send_keys(int(manager_id))


@when('The Manager types {message} into the message box')
def message_input(context, message: str):
    context.manager_form.message().send_keys(message)


@when('The Manager clicks the submit button')
def submit_edited(context):
    context.manager_form.save().click()


@when('The Manager clicks the return to home page button')
def back_to_home(context):
    context.manager_form.return_to_portal().click()
