*** Settings ***
Test Teardown    Delete dataset case teardown
Resource         ../../resources/gui/generic-resources.robot

*** Variables ***
${DATASET_NAME}    dataset-1
@{ITEMS}           {"key-a1": "value-a1", "key-a2": "value-a2"}
...                {"key-b1": "value-b1", "key-b2": "value-b2"}

*** Test Cases ***
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
    [Setup]    set multiple test variables    DELETED_ITEM=${ITEMS}[0]    EXISTING_ITEM=${ITEMS}[1]
    Given "next" dataset was configured
    When user clicks dataset item delete button
    Then conformation alert for item with information will be shown

Delete dataset item will remove dataset from database
    [Setup]    set multiple test variables    DELETED_ITEM=${ITEMS}[0]    EXISTING_ITEM=${ITEMS}[1]
    Given "next" dataset was configured
    When user clicks dataset item delete button
    And user confirms deleting
    Then dataset item will be removed from database
    And other dataset items will be left in database
    
Delete dataset item will remove dataset from existing dataset list
    [Setup]    set multiple test variables    DELETED_ITEM=${ITEMS}[0]    EXISTING_ITEM=${ITEMS}[1]
    Given "next" dataset was configured
    When user clicks dataset item delete button
    And user confirms deleting
    Then dataset item will be removed from existing dataset list
    And other dataset items will be left in existing dataset list

Toggle dataset will hide add item container 
    [Setup]    Set Test Variable    ${DATATYPE}    next
    Given dataset section was open
    And add item container was visible
    When user clicks dataset
    Then add item container will be hidden

Stop button will set item as out of use
    [Setup]    Set Test Variable    ${DATATYPE}    next
    Given dataset section was open
    When user clicks item "stop" button
    Then item will be set as out of use
    And button will be changed to "play"

Play button will set item as available
    [Setup]    Set Test Variable    ${DATATYPE}    next
    Given dataset section was open
    And item was out of use
    When user clicks item "play" button
    Then item will be set as available
    And button will be changed to "stop"
