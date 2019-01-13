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
GET /testdata/<dataset> will response with status code 200 and next dataset item 
    [Setup]    Set Test Variable    ${DATASET_NAME}    ${DATASET_NAMES}[0]
    Given testdata was configured
    And dataset item was requested
    When GET /testdata/<dataset> request is send
    Then status code 200 with next dataset item will be received

DELETE /testdata/<dataset> will response with status code 200
    [Setup]    Set Test Variable    ${DATASET_NAME}    ${DATASET_NAMES}[0]
    Given testdata was configured
    When DELETE /testdata/<dataset> request is send
    Then status code "200" will be received
    
DELETE /testdata/<dataset>/<item> will response with status code 200
    [Setup]    Set dataset variables    ${DATASET_NAMES}[0]    ${ITEMS_0}[0]
    Given testdata was configured
    When DELETE /testdata/<dataset>/<item> request is send
    Then status code "200" will be received
