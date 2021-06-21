from behave import given, when, then


@given('The Employee is on the New request form page')
def open_request_form(context):
    context.driver.get("C:\\Users\\david\\Documents\\ExpenseReimbursementFrontend\\submitrequest.html")


@given('The Employee has clicked the submit new request button')
def click_request(context):
    context.employee_portal.submit_request_button().click()


@when('The Employee types {amount} into the amount bar')
def amount_input(context, amount: str):
    context.employee_form.amount().send_keys(amount)


@when('The Employee types {reason} into the reason bar')
def reason_input(context, reason: str):
    context.employee_form.reason().send_keys(reason)


@when('The Employee clicks the submit button')
def submit_req(context):
    context.employee_form.submit().click()


@when('The Employee clicks the return to home page button')
def to_portal(context):
    context.employee_form.return_to_portal().click()
