from actionsLocatorsUtils.commons.Commons import Commons
from actionsLocatorsUtils.locators.genericLocators import genericLocators
from actionsLocatorsUtils.locators.modelHubLocators import modelHubLocators
from selenium.webdriver.common.by import By
import warnings


class llmModel:

    def __init__(self, driver):
        self.driver = driver
        self.modelHubL = modelHubLocators(driver)
        self.common = Commons(driver)
        self.generic = genericLocators(driver)

    def createNewLLMModel(self, ModelName, Modelprovider, ModelID):

        #---- work starts for ModelName----#
        self.modelHubL.modelName().send_keys(ModelName)
        self.common.pause(2)
        #---- work starts for ModelProvider----#
        self.modelHubL.modelProvider().click()
        self.common.pause(1)
        contentTable = self.common.waitForVisibility(self.modelHubL.modelContent())
        if contentTable.is_displayed():
            print("Content table is displayed")
        else:
            assert False, "Content table is not visible"
        # self.common.pause(1)
        self.modelHubL.selectModelProvider_ID(Modelprovider).click()
        self.common.pause(1)
        # string = self.modelHubL.getSelectedModelText().text
        # if Modelprovider.lower() == string.lower():
        #     print("Validation Pased: Option selected is "+Modelprovider)
        # else:
        #     warnings.warn("Validation Failed, Option selected doesnt match with the expected value")

        #---- work starts for ModelID ----#
        self.modelHubL.modelID().click()
        contentTable =self.common.waitForVisibility(self.modelHubL.modelContent())
        if contentTable.is_displayed():
            print("Content table is displayed")
        else:
            assert False, "Content table is not visible"
        # self.common.pause(1)
        self.modelHubL.selectModelProvider_ID(ModelID).click()
        # self.common.pause(1)
        # string1 = self.modelHubL.getSelectedModelIDText().text
        # if ModelID.lower() == string1.lower():
        #     print("Validation Pased: Option selected is "+ModelID)
        # else:
        #     warnings.warn("Validation Failed, Option selected is not as expected")

        #--- save ---#
        self.common.pause(1)
        self.generic.button("Save").click()

        #----- check for saved ones ---#
        self.common.pause(1)
        try:
            save = self.common.waitForVisibility(self.modelHubL.checkSavedLLMModle(ModelName))
            if save.is_displayed():
                print("Validation Passed: Saved LLM is visible with model name "+ModelName)
            else:
                assert False, "Validation Failed: Saved LLM is not visible"
        except Exception as s:
            print("Exception has occured:" + s)



    def testingResponse(self, ModelName):

        self.driver.refresh()
        self.common.pause(5)
        self.modelHubL.viewModel(ModelName).click()
        if self.common.waitForVisibility(self.modelHubL.newLLMTitle(ModelName)).is_displayed():
            print("Validation Passed: "+ModelName+" is open after view model click")
        else:
            assert False, "Validation Failed: Incorrect model is open"

        self.generic.button("Test endpoint").click()
        if self.common.waitForVisibility(self.modelHubL.dialogBox()).is_displayed():
            print("Validation Passed: Dialogbox is open when Test endpoint is clicked")
        else:
            assert False, "Validation Failed: Dialog box is not present"
        # self.common.zoomOut(self.driver, "75%")
        self.modelHubL.requestTextBox().send_keys("Hello")
        self.common.pause(3)

        self.modelHubL.sendRequest().click()
        if self.common.waitForVisibility(self.modelHubL.checkResponse()).is_displayed():
            print("Validation Passed: Response is generated")
        else:
            assert False, "Validation Failed, response is not generated"
        self.common.pause(2)
        self.driver.find_element(By.XPATH, self.modelHubL.closeTestEndPoint()).click()
        try:

            if not self.common.waitForVisibility(self.modelHubL.closeTestEndPoint()):
                    print("Validation Passed: Test endpoint tab is closed when Test endpoint button is clicked")
            else:
                warnings.warn("Validation Failed: Test endpoint tab is not closed when Test endpoint close button is clicked")
        except Exception as e:
                print("Test endpoint tab is closed")


    def deleteModel(self):

        self.common.pause(1)
        self.modelHubL.deleteButton().click()
        if self.common.waitForVisibility(self.modelHubL.deleteTab()).is_displayed():
            print("Validation Passed: Delete tab is open once delete button is clicked")
        else:
            assert False, "Validation Failed: Delete tab is not visible after clicking on delete button"

        self.common.pause(1)
        self.modelHubL.deleteTabOkBtn().click()
        self.common.pause(1)
        if self.common.waitForVisibility(self.modelHubL.llmTab()).is_displayed():
            print("Validation Passed: LLM tab is displayed after LLM model delete button is clicked")
        else:
            assert False, "Validation Failed: LLM tab is not displayed after LLM model is deleted"

        if self.driver.find_element(By.XPATH, self.modelHubL.newLLMTitle("No LLM Models yet")).is_displayed():
            print("Validation Passed: No LLM model is present once deleted")
        else:
            warnings.warn("Validation Failed: LLM model is present after deleting as well.")













