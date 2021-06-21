from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class ManagerPortal:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def view_request_button(self):
        element: WebElement = self.driver.find_element_by_id("6")
        return element

    def logout_button(self):
        element: WebElement = self.driver.find_element_by_id("logout")
        return element

    def view_stats(self):
        element: WebElement = self.driver.find_element_by_id("stats")
        return element
