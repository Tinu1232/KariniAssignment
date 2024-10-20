from selenium.webdriver.common.by import By

class genericLocators:

    def __init__(self, driver):
        self.driver = driver

    def button(self, type):
        return self.driver.find_element(By.XPATH, "//button[text()='"+type+"']")