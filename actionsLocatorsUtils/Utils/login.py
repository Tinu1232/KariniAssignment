from actionsLocatorsUtils.commons.Commons import Commons
from actionsLocatorsUtils.locators.dashboardlocators import *
from actionsLocatorsUtils.locators.loginLocators import *

class login:

    def __init__(self, driver):
        self.driver = driver
        self.locators = loginLocators(driver)
        self.commons = Commons(driver)
        self.dashboard = dashboardLocators(driver)

    def enterEmailID(self, email, passwordd):
        emailID = self.locators.emailID()
        password = self.locators.password()
        submit = self.locators.submit()
        emailID.send_keys(email)
        password.send_keys(passwordd)
        submit.click()
        dash = self.commons.waitForVisibility(self.dashboard.dashboard())
        if dash.is_displayed():
            print("Validation Passed: Login is successfull")
        else:
            assert False, "Validation Failed: Login is not successfull"


