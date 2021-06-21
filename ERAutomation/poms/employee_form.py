from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class EmployeeForm:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def amount(self):
        element: WebElement = self.driver.find_element_by_id("amountInput")
        return element

    def reason(self):
        element: WebElement = self.driver.find_element_by_id("reasonInput")
        return element

    def submit(self):
        element: WebElement = self.driver.find_element_by_id("submit")
        return element

    def return_to_portal(self):
        element: WebElement = self.driver.find_element_by_id("toHome")
        return element
