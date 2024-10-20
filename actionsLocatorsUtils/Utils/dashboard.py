
from selenium.webdriver.common.action_chains import ActionChains
from actionsLocatorsUtils.commons.Commons import *
from actionsLocatorsUtils.locators.dashboardlocators import *
from actionsLocatorsUtils.locators.modelHubLocators import *
class dashboard:

    def __init__(self, driver):
        self.driver = driver
        self.dashB = dashboardLocators(driver)
        self.common = Commons(driver)
        self.modelHub = modelHubLocators(driver)

    def selectModelHubIcon(self):
        modelIncn = self.dashB.modelHubIcon()
        modelIncn.click()
        print("Model Hub icon is clicked")

    def selectLLMEndPoint(self):
        selectLLM = self.dashB.llmModelEndPoint()
        actions = ActionChains(self.driver)
        actions.click(selectLLM).perform()
        noLLMtext = self.common.waitForVisibility(self.dashB.noLLMModelTxt())
        if noLLMtext.is_displayed():
            print("Validation Passed: User is on the LLM model")
        else:
            assert False, "Valdiation Failed: User is not on the LLM model after clicking on LLM"

    def addNewModel(self):
        addNewBtn = self.common.waitForVisibility(self.dashB.addNew())
        if addNewBtn.is_displayed():
            print("Validation Passed: AddNew+ button is visible ")
        else:
            assert False, "Validation Failed: AddNew button is missing"
        self.common.pause(2)
        addNewBttn = self.dashB.addNewBtn()
        addNewBttn.click()

        newAdded = self.common.waitForVisibility(self.modelHub.newLLMTitle("Add new"))
        if newAdded.is_displayed():
            print("Validation Passed: Add new title is visible once add new button is clicked")
        else:
            assert False, "Validation Failed, Add new title is not present after clicking on Add new button"

