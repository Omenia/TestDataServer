*** Settings ***
Test Teardown    Delete dataset case teardown
Resource         ../../resources/gui/generic-resources.robot

*** Variables ***
${DATASET_NAME}    dataset-1
@{ITEMS}           {"key-a1": "value-a1", "key-a2": "value-a2"}
...                {"key-b1": "value-b1", "key-b2": "value-b2"}

*** Test Cases ***
Next datatype - New dataset will be stored to database
    Given add new dataset section was open
    When user submits new "next" dataset
    Then dataset will be stored to database

Random datatype - New dataset will be stored to database
    Given add new dataset section was open
    When user submits new "random" dataset
    Then dataset will be stored to database

New dataset will be added to existing dataset list
    Given add new dataset section was open
    When user submits new "next" dataset
    Then dataset will be added to existing dataset list

