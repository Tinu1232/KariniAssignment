from Utils.dashboard import dashboard
from Utils.llmModel import llmModel
from Utils.login import login
from behave import given
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from commons.Commons import Commons

@given('I login to the Karini AI website with email "{email}" and password "{password}"')
def loginmethod(context, email, password):
    log = login(context.driver)
    log.enterEmailID(email, password)


@given('I launch the chrome browser and open Karini AI')
def launchbrowser(context):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()
    context.driver.implicitly_wait(15)
    commons = Commons(context.driver)
    commons.launchURL("https://app.karini.ai/signin")


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
def step_impl(context, modelName, modelProvider, modelID):
    llm = llmModel(context.driver)
    llm.createNewLLMModel(modelName, modelProvider, modelID)


@given('I test the Testing End Point for Model "{modeName}"')
def testModel(context, modeName):
    llm = llmModel(context.driver)
    llm.testingResponse(modeName)


@given('I delete the model')
def step_impl(context):
    llm = llmModel(context.driver)
    llm.deleteModel()

