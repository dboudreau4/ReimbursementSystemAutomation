from behave import given, when, then


@given('The Manager is on the Statistics Page')
def open_stats_page(context):
    context.driver.get("C:\\Users\\david\\Documents\\ExpenseReimbursementFrontend\\statspage.html")


@when('The Manager clicks on Return to Manager Portal Button')
def back_to_portal(context):
    context.manager_stats.return_to_portal().click()


@when('The Manager clicks on the stats log out button')
def sign_out(context):
    context.manager_stats.logout_button().click()
