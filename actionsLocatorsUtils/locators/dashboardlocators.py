from selenium.webdriver.common.by import By


class dashboardLocators:

    def __init__(self, driver):
        self.driver = driver

    def dashboard(self):
        return "//h1[text()='Dashboards']"

    def modelHubIcon(self):
        return self.driver.find_element(By.XPATH, "//a[@href='/model']")

    def llmModelEndPoint(self):
        return self.driver.find_element(By.XPATH, "//button[@data-key='llm_model']")

    def addNew(self):
        return "//button[@aria-label='Add new']"

    def addNewBtn(self):
        return self.driver.find_element(By.XPATH, "//button[@aria-label='Add new']")

    def noLLMModelTxt(self):
        return "//h3[text()='No LLM Models yet']"
