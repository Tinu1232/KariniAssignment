from selenium.webdriver.common.by import By

class loginLocators:

    def __init__(self, driver):
        self.driver = driver

    def emailID(self):
        return self.driver.find_element(By.XPATH, "//input[@aria-label='Email']")

    def password(self):
        return self.driver.find_element(By.XPATH, "//input[@aria-label='Password']")

    def submit(self):
        return self.driver.find_element(By.XPATH, "//button[text()='Submit']")

