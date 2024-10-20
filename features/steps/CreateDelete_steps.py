from actionsLocatorsUtils.Utils.dashboard import dashboard
from actionsLocatorsUtils.Utils.llmModel import llmModel
from actionsLocatorsUtils.Utils.login import login
from behave import given
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from actionsLocatorsUtils.commons.Commons import Commons
import os
import glob


@given('I launch the chrome browser and open Karini AI')
def launchbrowser(context):
    directory = "actionsLocatorsUtils/Test/"
    csv_files = glob.glob(os.path.join(directory, "*.csv"))
    if not csv_files:
        print("No CSV files found to delete.")
    else:
        for file_path in csv_files:
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()
    context.driver.implicitly_wait(60)
    commons = Commons(context.driver)
    commons.launchURL("https://app.karini.ai/signin")



@given('I login to the Karini AI website with email "{email}" and password "{password}"')
def loginmethod(context, email, password):
    log = login(context.driver)
    log.enterEmailID(email, password)

@given('I click on Model Hub Icon')
def clickOnModelHub(context):
    dash = dashboard(context.driver)
    dash.selectModelHubIcon()


@given('I go the LLM end points')
def goToLLM(context):
    dash = dashboard(context.driver)
    dash.selectLLMEndPoint()


@given('I add a new model')
def addNewModel(context):
    dash = dashboard(context.driver)
    dash.addNewModel()


@given('I create model with details as Model Name "{modelName}", Model Provider "{modelProvider}", ModelID "{modelID}"')
def createNewModel(context, modelName, modelProvider, modelID):
    llm = llmModel(context.driver)
    llm.createNewLLMModel(modelName, modelProvider, modelID)


@given('I test the Testing End Point for Model "{modeName}"')
def testModel(context, modeName):
    llm = llmModel(context.driver)
    llm.testingResponse(modeName)


@given('I delete the model')
def deleteModel(context):
    llm = llmModel(context.driver)
    llm.deleteModel()

