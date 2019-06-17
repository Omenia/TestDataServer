*** Settings ***
Test Teardown    Delete dataset case teardown
Resource         ../../resources/api/generic-resources.robot

*** Variables ***
@{DATASET_NAMES}=    dataset-1    dataset-2
@{ITEMS_0}=          {"key-a1": "value-a1", "key-a2": "value-a2"}
...                  {"key-b1": "value-b1", "key-b2": "value-b2"}
@{ITEMS_1}=          {"key-z1": "value-z1", "key-z2": "value-z2"}
...                  {"key-x1": "value-x1", "key-x2": "value-x2"}
&{NEXT_DATASET}=      dataset=${DATASET_NAMES}[0]    datatype=next     items=@{ITEMS_0}
&{RANDOM_DATASET}=    dataset=${DATASET_NAMES}[1]    datatype=random    items=@{ITEMS_1}
@{ALL_DATASETS}=      &{NEXT_DATASET}    &{RANDOM_DATASET}

*** Test Cases ***
GET /testdata will response with status code 200 and datasets
    Given testdata was configured
    When GET "/testdata" request is send
    Then status code 200 with datasets will be received

POST /testdata with dataset will response with status code 201
    [Setup]    Set Test Variable    
     ...    ${PARAMS}    {"dataset": "${DATASET_NAMES}[0]", "items": [${ITEMS_0}[0], ${ITEMS_0}[1]], "datatype": "next"}
    Given service was running
    When POST /testdata request with dataset is send
    Then status code "201" will be received

Missing dataset parameter - POST /testdata will response with status code 400
    [Setup]    Set Test Variable    ${PARAMS}    {"items": [${ITEMS_0}[0], ${ITEMS_0}[1]], "datatype": "next"}
    Given service was running
    When POST /testdata request without dataset parameter is send
    Then status code "400" will be received with error "'dataset' is a required property" 

Existing dataset - POST /testdata with dataset will response with status code 409
    [Setup]    Set Test Variable    
     ...    ${PARAMS}    {"dataset": "${DATASET_NAMES}[0]", "items": [${ITEMS_0}[0], ${ITEMS_0}[1]], "datatype": "next"}
    Given testdata was configured
    When POST /testdata request with existing dataset is send
    Then status code "409" will be received with error "dataset exists already" 

Missing items parameter - POST /testdata will response with status code 400
    [Setup]    Set Test Variable    ${PARAMS}    {"dataset": "${DATASET_NAMES}[0]", "datatype": "next"}
    Given service was running
    When POST /testdata request without dataset parameter is send
    Then status code "400" will be received with error "'items' is a required property" 

Missing datatype parameter - POST /testdata will response with status code 400
    [Setup]    Set Test Variable
    ...    ${PARAMS}    {"dataset": "${DATASET_NAMES}[0]", "items": [${ITEMS_0}[0], ${ITEMS_0}[1]]}
    Given service was running
    When POST /testdata request without datatype parameter is send
    Then status code "400" will be received with error "'datatype' is a required property"

Unsupported datatype parameter - POST /testdata will response with status code 400
    [Setup]    Set Test Variable
    ...    ${PARAMS}    {"dataset": "${DATASET_NAMES}[0]", "items": [${ITEMS_0}[0], ${ITEMS_0}[1]], "datatype": "unsupported"}
    Given service was running
    When POST /testdata request with unsupported datatype parameter is send
    Then status code "400" will be received with error "unsupported 'datatype'"
