from selenium.webdriver.common.by import By


class modelHubLocators:

    def __init__(self, driver):
        self.driver = driver

    def newLLMTitle(self, text):
        return "//h3[text()='"+text+"']"

    def modelName(self):
        return self.driver.find_element(By.XPATH, "//input[@aria-label='Model name']")

    def modelProvider(self):
        return self.driver.find_element(By.XPATH, "//label[text()='Model provider']//following-sibling::div")

    def modelContent(self):
        return "//div[@data-slot='content']"

    def selectModelProvider_ID(self, model):
        return self.driver.find_element(By.XPATH, "//span[text()='"+model+"']")

    def getSelectedModelText(self):
        return self.driver.find_element(By.XPATH, "//label[text()='Model provider']//following-sibling::div/span")

    def modelID(self):
        return self.driver.find_element(By.XPATH, "//label[text()='Model id']//following-sibling::div")

    def getSelectedModelIDText(self):
        return self.driver.find_element(By.XPATH, "//label[text()='Model id']//following-sibling::div/span")

    def checkSavedLLMModle(self, ModelName):
        return "//div[contains(@class, 'grid')]/div/div/h2[text()='"+ModelName+"']"

    def viewModel(self, modelName):
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'grid')]/div/div/h2[text()='"+modelName+"']/../../div[2]/div[3]/a")

    def dialogBox(self):
        return "//section[@role='dialog']"

    def requestTextBox(self):
        return self.driver.find_element(By.XPATH, "//div/label[text()='Request']/../../div[2]/div/textarea")

    def sendRequest(self):
        return self.driver.find_element(By.XPATH, "//button[text()='Send request']")

    def checkResponse(self):
        return "//div/label[text()='Response']/../../div[2]/div/textarea[@data-filled='true']"

    def closeTestEndPoint(self):
        return "//section/button[@aria-label='Close']"

    def deleteButton(self):
        return self.driver.find_element(By.XPATH, "//button[text()='Delete']")

    def deleteTab(self):
        return "//section/header[text()='Delete']"

    def deleteTabOkBtn(self):
        return self.driver.find_element(By.XPATH, "//section/header[text()='Delete']/following-sibling::footer/div/div/div/button[text()='Ok']")

    def llmTab(self):
        return "//button[@data-key='llm_model']"