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
DELETE /testdata/<dataset>/<item> will response with status code 200
    [Setup]    Set dataset variables    ${DATASET_NAMES}[0]    ${ITEMS_0}[0]
    Given testdata was configured
    When DELETE /testdata/<dataset>/<item> request is send
    Then status code "200" will be received

Unknown item - DELETE /testdata/<dataset>/<item> will response with status code 404
    [Setup]    Set dataset variables    ${DATASET_NAMES}[0]    {"unknown": "item"}
    Given testdata was configured
    When DELETE /testdata/<dataset>/<item> request with unknown item is send
    Then status code "404" will be received with error "dataset item does not exist" 

Item not in json - DELETE /testdata/<dataset>/<item> will response with status code 400
    [Setup]    Set dataset variables    ${DATASET_NAMES}[0]    not-json
    Given testdata was configured
    When DELETE /testdata/<dataset>/<item> request with not json item is send
    Then status code "400" will be received with error "item is not json"

POST /testdata/<dataset>/<item> will response with status code 201
    [Setup]    Set dataset variables    ${DATASET_NAMES}[0]    {"new-item-key": "new-item-value"}
    Given testdata was configured
    When POST /testdata/<dataset>/<item> request is send
    Then status code "201" will be received

Unknown dataset - POST /testdata/<dataset>/<item> will response with status code 404
    [Setup]    Set dataset variables    unknown    {"new-item-key": "new-item-value"}
    Given testdata was configured
    When POST /testdata/<dataset>/<item> request is send
    Then status code "404" will be received with error "dataset does not exist"

Item not in json - POST /testdata/<dataset>/<item> will response with status code 400
    [Setup]    Set dataset variables    ${DATASET_NAMES}[0]    not-json
    Given testdata was configured
    When POST /testdata/<dataset>/<item> request with not json item is send
    Then status code "400" will be received with error "item is not json"

PUT /testdata/<dataset>/<item> will update item status
    [Setup]    Set dataset variables    ${DATASET_NAMES}[0]    ${ITEMS_0}[0]
    Given testdata was configured
    When PUT /testdata/<dataset>/<item> with request "out of use" is send
    Then item status in database will be "out of use"

Unknown item - PUT /testdata/<dataset>/<item> will response with status code 404
    [Setup]    Set dataset variables    ${DATASET_NAMES}[0]    {"unknown": "item"}
    Given testdata was configured
    When PUT /testdata/<dataset>/<item> with request "out of use" is send
    Then status code "404" will be received with error "item does not exist"

Item not in json - PUT /testdata/<dataset>/<item> will response with status code 400
    [Setup]    Set dataset variables    ${DATASET_NAMES}[0]    not-json
    Given testdata was configured
    When PUT /testdata/<dataset>/<item> with request "out of use" for not json item is send
    Then status code "400" will be received with error "item is not json"

Unsupported status parameter - PUT /testdata/<dataset>/<item> will response with status code 400
    [Setup]    Set dataset variables    ${DATASET_NAMES}[0]    ${ITEMS_0}[0]
    Given testdata was configured
    When PUT /testdata/<dataset>/<item> with request "unsupport" is send
    Then status code "400" will be received with error "unsupported 'status'"
