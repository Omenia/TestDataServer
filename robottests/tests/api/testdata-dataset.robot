*** Settings ***
Test Teardown    Delete dataset case teardown
Resource         ../../resources/api/generic-resources.robot

*** Variables ***
@{DATASET_NAMES}=     dataset-1    dataset-2
@{ITEMS_0}=           {"key-a1": "value-a1", "key-a2": "value-a2"}
...                   {"key-b1": "value-b1", "key-b2": "value-b2"}
@{ITEMS_1}=           {"key-z1": "value-z1", "key-z2": "value-z2"}
...                   {"key-x1": "value-x1", "key-x2": "value-x2"}
&{NEXT_DATASET}=      dataset=${DATASET_NAMES}[0]    datatype=next      items=@{ITEMS_0}
&{RANDOM_DATASET}=    dataset=${DATASET_NAMES}[1]    datatype=random    items=@{ITEMS_1}

*** Test Cases ***
Next - GET /testdata/<dataset> will response with status code 200 and next dataset item
    [Setup]    Set Test Variable    ${DATASET_NAME}    ${DATASET_NAMES}[0]
    Given testdata was configured
    And dataset item was requested
    When GET /testdata/<dataset> request is send
    Then status code 200 with next dataset item will be received

Random - GET /testdata/<dataset> will response with status code 200 and random dataset item
    [Setup]    Set Test Variable    ${DATASET_NAME}    ${DATASET_NAMES}[1]
    Given testdata was configured
    When GET /testdata/<dataset> request is send
    Then status code 200 with random dataset item will be received

Unknown dataset - GET /testdata/<dataset> will response with status code 404
    [Setup]    Set Test Variable    ${DATASET_NAME}    unknown
    Given testdata was configured
    When GET /testdata/<dataset> request with unknown dataset is send
    Then status code "404" will be received with error "dataset does not exist" 

Next - No available items - GET /testdata/<dataset> will response with status code 409
    [Setup]    set multiple test variables    DATASET_NAME=${DATASET_NAMES}[0]    ITEMS=${ITEMS_0}
    Given testdata was configured
    And all items were out of use
    When GET /testdata/<dataset> request is send
    Then status code "409" will be received with error "no items available"

DELETE /testdata/<dataset> will response with status code 200
    [Setup]    Set Test Variable    ${DATASET_NAME}    ${DATASET_NAMES}[0]
    Given testdata was configured
    When DELETE /testdata/<dataset> request is send
    Then status code "200" will be received

Unknown dataset - DELETE /testdata/<dataset> will response with status code 404
    [Setup]    Set Test Variable    ${DATASET_NAME}    unknown
    Given testdata was configured
    When DELETE /testdata/<dataset> request with unknown dataset is send
    Then status code "404" will be received with error "dataset does not exist" 
