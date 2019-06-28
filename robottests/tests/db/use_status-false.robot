*** Settings ***
Test Teardown     Delete dataset case teardown
Resource          ../../resources/api/generic-resources.robot

*** Variables ***
@{DATASET_NAMES}=     dataset-1    dataset-2
@{ITEMS_0}=           {"key-a1": "value-a1", "key-a2": "value-a2"}
...                   {"key-b1": "value-b1", "key-b2": "value-b2"}
@{ITEMS_1}=           {"key-z1": "value-z1", "key-z2": "value-z2"}
...                   {"key-x1": "value-x1", "key-x2": "value-x2"}
&{NEXT_DATASET}=      dataset=${DATASET_NAMES}[0]    datatype=next      items=@{ITEMS_0}
&{RANDOM_DATASET}=    dataset=${DATASET_NAMES}[1]    datatype=random    items=@{ITEMS_1}

*** Test Cases ***
Next - GET /testdata/<dataset> will not set item as reserved
    [Setup]    set multiple test variables    DATASET_NAME=${DATASET_NAMES}[0]    ITEM=${ITEMS_0}[0]
    Given testdata was configured
    When GET /testdata/<dataset> request is send
    Then item status in database will be "available"
