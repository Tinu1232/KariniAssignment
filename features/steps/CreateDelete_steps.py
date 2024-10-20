from Utils.login import login
from behave import given, when, then
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from commons.Commons import Commons

@given("I login to the Karini AI webiste with email {email} and password {password}")
def loginmethod(context, email, password):
    log = login(context)
    log.enterEmailID(email, password)


@given(u'I launch the chrome brower and open Karini AI')
def launchbrowser(context):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()
    context.driver.implicitly_wait(15)
    commons = Commons(context.driver)
    commons.launchURL("https://app.karini.ai/signin")


@given('I click on Model Hub Icon')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I click on Model Hub Icon')


@given('I go the LLM end points')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I go the LLM end points')


@given('I add a new model')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I add a new model')


@given('I create model with details as ModelName "OPENAI GPT 4O Mini", Modelprovider "OpenAI", ModelID "GPT 4O Mini"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I create model with details as ModelName "OPENAI GPT 4O Mini", Modelprovider "OpenAI", ModelID "GPT 4O Mini"')


@given('I test the Testing End Point for Model "OPENAI GPT 4O Mini"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I test the Testing End Point for Model "OPENAI GPT 4O Mini"')


@given('I delete the model')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I delete the model')


@given('I create model with details as ModelName "OPENAI GPT 4O", Modelprovider "OpenAI", ModelID "GPT 4O"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I create model with details as ModelName "OPENAI GPT 4O", Modelprovider "OpenAI", ModelID "GPT 4O"')


@given('I test the Testing End Point for Model "OPENAI GPT 4O"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I test the Testing End Point for Model "OPENAI GPT 4O"')
