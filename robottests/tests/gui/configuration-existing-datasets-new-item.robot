*** Settings ***
Test Teardown    Delete dataset case teardown
Resource         ../../resources/gui/generic-resources.robot

*** Variables ***
${DATASET_NAME}    dataset-1
@{ITEMS}           {"key-a1": "value-a1", "key-a2": "value-a2"}
...                {"key-b1": "value-b1", "key-b2": "value-b2"}

*** Test Cases ***
New dataset item will be stored to database
    [Setup]    set multiple test variables    
    ...    NEW_ITEM={"new-key-1": "new-value-1", "new-key-2": "new-value-2"}    
    ...    DATATYPE=next
    Given dataset section was open
    When user clicks add item icon
    And user submits new item
    Then dataset item will be stored to database

New dataset item will be added to existing dataset item list
    [Setup]    set multiple test variables    
    ...    NEW_ITEM={"new-key-1": "new-value-1", "new-key-2": "new-value-2"}    
    ...    DATATYPE=next 
    Given dataset section was open
    When user clicks add item icon
    And user submits new item
    Then item will be added to existing dataset item list

Toggle add item icon will hide add item container
    [Setup]    Set Test Variable    ${DATATYPE}    next
    Given dataset section was open
    When user clicks add item icon
    Then add item container will be hidden
