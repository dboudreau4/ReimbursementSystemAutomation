from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class EmployeePortal:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def submit_request_button(self):
        element: WebElement = self.driver.find_element_by_id("submitBtn")
        return element

    def logout_button(self):
        element: WebElement = self.driver.find_element_by_id("logout")
        return element
