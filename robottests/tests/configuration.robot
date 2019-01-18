*** Settings ***
Test Teardown    Delete dataset case teardown
Resource         ../resources/generic-resources.robot

*** Variables ***
${DATASET_NAME}    dataset-1
@{ITEMS}           "key-a1": "value-a1", "key-a2": "value-a2"
...                "key-b1": "value-b1", "key-b2": "value-b2"

*** Test Cases ***
New dataset will be stored to database
    Given user was on "configuration page"
    When user submits new dataset
    Then dataset will be stored to database

Delete dataset button will show alert for conformation
    Given dataset was configured
    When user clicks dataset delete button
    Then conformation alert for dataset with information will be shown

Delete dataset button will remove dataset from database
    Given dataset was configured
    When user clicks dataset delete button
    And user confirms deleting
    Then dataset will be removed from database

Delete dataset item button will show alert for conformation
    Given dataset was configured
    When user clicks dataset item delete button
    Then conformation alert for item with information will be shown

Delete dataset item button will remove dataset from database
    Given dataset was configured
    When user clicks dataset item delete button
    And user confirms deleting
    Then dataset item will be removed from database
    And other dataset items will be left in database
    