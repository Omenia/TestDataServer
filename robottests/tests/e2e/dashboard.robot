*** Settings ***
Test Teardown    Delete dataset case teardown
Resource         ../../resources/e2e/generic-resources.robot

*** Variables ***
${DATASET_NAME}    dataset-1
@{ITEMS}           {"key-a1": "value-a1", "key-a2": "value-a2"}
...                {"key-b1": "value-b1", "key-b2": "value-b2"}

*** Test Cases ***
Dataset will be shown in dashboard
    [Setup]    Set Test Variable    ${STATUS}    available
    Given "next" dataset was configured
    When user visits dashboard page
    Then dataset will be shown in dashboard
