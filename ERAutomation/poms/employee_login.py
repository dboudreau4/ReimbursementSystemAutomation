from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class EmployeeLogin:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def username(self):
        element: WebElement = self.driver.find_element_by_id("usernameInput")
        return element

    def password(self):
        element: WebElement = self.driver.find_element_by_id("passwordInput")
        return element

    def login_button(self):
        element: WebElement = self.driver.find_element_by_id("login")
        return element
