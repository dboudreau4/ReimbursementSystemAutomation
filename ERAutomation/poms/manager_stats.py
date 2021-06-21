from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class ManagerStats:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def return_to_portal(self):
        element: WebElement = self.driver.find_element_by_id("toHome")
        return element

    def logout_button(self):
        element: WebElement = self.driver.find_element_by_id("logout")
        return element
