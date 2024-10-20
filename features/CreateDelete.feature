Feature: Create a new LLM model and test end point response and delete it

  Scenario: Login to the karini AI website and go to Model HUB and create a new LLM model in LLM section and delete it once testing end point is done
    Given I launch the chrome browser and open Karini AI
    And I login to the Karini AI website with email "rajpurohitnilesh103@gmail.com" and password "Welcome1!"
    And I click on Model Hub Icon
    And I go the LLM end points
    And I add a new model
    And I create model with details as Model Name "OPENAI GPT 4O Mini", Model Provider "OpenAI", ModelID "GPT 4O Mini"
    And I test the Testing End Point for Model "OPENAI GPT 4O Mini"
    And I delete the model
    And I add a new model
    And I create model with details as Model Name "OPENAI GPT 4O", Model Provider "OpenAI", ModelID "GPT 4O"
    And I test the Testing End Point for Model "OPENAI GPT 4O"
    And I delete the model



