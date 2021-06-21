from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select


class ManagerForm:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select(self):
        element: Select = Select(self.driver.find_element_by_id("status-select"))
        return element

    def manager_id(self):
        element: WebElement = self.driver.find_element_by_id("managerId")
        return element

    def message(self):
        element: WebElement = self.driver.find_element_by_id("message")
        return element

    def save(self):
        element: WebElement = self.driver.find_element_by_id("save")
        return element

    def return_to_portal(self):
        element: WebElement = self.driver.find_element_by_id("toHome")
        return element
