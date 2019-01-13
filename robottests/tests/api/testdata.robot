*** Settings ***
Test Teardown    Delete dataset case teardown
Resource         ../../resources/api/generic-resources.robot

*** Variables ***
@{DATASET_NAMES}=    dataset-1    dataset-2
@{ITEMS_0}=          {"key-a1": "value-a1", "key-a2": "value-a2"}
...                  {"key-b1": "value-b1", "key-b2": "value-b2"}
@{ITEMS_1}=          {"key-z1": "value-z1", "key-z2": "value-z2"}
...                  {"key-x1": "value-x1", "key-x2": "value-x2"}
&{DATASETS}=         ${DATASET_NAMES}[0]=@{ITEMS_0}    ${DATASET_NAMES}[1]=@{ITEMS_1}

*** Test Cases ***
GET /testdata will response with status code 200 and datasets
    Given testdata was configured
    When GET "/testdata" request is send
    Then status code 200 with datasets will be received

POST /testdata with dataset will response with status code 201
    [Setup]    Set Test Variable    
     ...    ${BODY}    {"dataset": "${DATASET_NAMES}[0]", "items": [${ITEMS_0}[0], ${ITEMS_0}[1]]}
    Given service was running
    When POST /testdata request with dataset is send
    Then status code "201" will be received
    