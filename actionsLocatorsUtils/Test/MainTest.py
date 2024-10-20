
from actionsLocatorsUtils.Utils.dashboard import dashboard
from actionsLocatorsUtils.Utils.llmModel import llmModel
from actionsLocatorsUtils.Utils.login import login
from actionsLocatorsUtils.commons.Commons import Commons
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
# import unittest

#--main run---
chrome_options = Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(15)

log = login(driver)
commons = Commons(driver)
dash = dashboard(driver)
llm = llmModel(driver)

commons.launchURL("https://app.karini.ai/signin")
log.enterEmailID("rajpurohitnilesh103@gmail.com", "Welcome1!")
commons.zoomOut(driver, "75%")
dash.selectModelHubIcon()
dash.selectLLMEndPoint()
dash.addNewModel()
llm.createNewLLMModel("OPENAI GPT 4O Mini", "OpenAI", "GPT 4O Mini")
llm.testingResponse("OPENAI GPT 4O Mini")
llm.deleteModel()
dash.addNewModel()
llm.createNewLLMModel("OPENAI GPT 4O", "OpenAI", "GPT 4O")
llm.testingResponse("OPENAI GPT 4O")
llm.deleteModel()




