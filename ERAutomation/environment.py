from behave.runner import Context
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from poms.employee_form import EmployeeForm
from poms.employee_login import EmployeeLogin
from poms.employee_portal import EmployeePortal
from poms.manager_form import ManagerForm
from poms.manager_login import ManagerLogin
from poms.manager_portal import ManagerPortal
from poms.manager_stats import ManagerStats


def before_all(context: Context):
    context.driver = webdriver.Chrome('C:\\Users\\david\\Desktop\\Drivers\\chromedriver.exe')
    context.driver.implicitly_wait(10)
    context.employee_login = EmployeeLogin(context.driver)
    context.employee_portal = EmployeePortal(context.driver)
    context.employee_form = EmployeeForm(context.driver)
    context.manager_login = ManagerLogin(context.driver)
    context.manager_portal = ManagerPortal(context.driver)
    context.manager_form = ManagerForm(context.driver)
    context.manager_stats = ManagerStats(context.driver)


def after_all(context):
    context.driver.quit()
