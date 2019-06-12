*** Settings ***
Test Teardown    Delete dataset case teardown
Resource         ../../resources/e2e/generic-resources.robot

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

Deleting dataset will show alert for conformation
    Given "next" dataset was configured
    When user clicks dataset delete button
    Then conformation alert for dataset with information will be shown
    [Teardown]    Sleep    0.1    reason=To prevent next case to be started too soon

Delete dataset will remove dataset from database
    Given "next" dataset was configured
    When user clicks dataset delete button
    And user confirms deleting
    Then dataset will be removed from database

Delete dataset will remove dataset from existing dataset list
    Given "next" dataset was configured
    When user clicks dataset delete button
    And user confirms deleting
    Then dataset will be removed from existing dataset list

Deleting dataset item will show alert for conformation
    Given "next" dataset was configured
    When user clicks dataset item delete button
    Then conformation alert for item with information will be shown

Delete dataset item will remove dataset from database
    Given "next" dataset was configured
    When user clicks dataset item delete button
    And user confirms deleting
    Then dataset item will be removed from database
    And other dataset items will be left in database
    
Delete dataset item will remove dataset from existing dataset list
    Given "next" dataset was configured
    When user clicks dataset item delete button
    And user confirms deleting
    Then dataset item will be removed from existing dataset list
    And other dataset items will be left in existing dataset list

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

Toggle dataset will hide add item container 
    [Setup]    Set Test Variable    ${DATATYPE}    next
    Given dataset section was open
    And add item container was visible
    When user clicks dataset
    Then add item container will be hidden

