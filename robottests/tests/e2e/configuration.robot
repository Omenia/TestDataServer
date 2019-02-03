*** Settings ***
Test Teardown    Delete dataset case teardown
Resource         ../../resources/e2e/generic-resources.robot

*** Variables ***
${DATASET_NAME}    dataset-1
@{ITEMS}           {"key-a1": "value-a1", "key-a2": "value-a2"}
...                {"key-b1": "value-b1", "key-b2": "value-b2"}

*** Test Cases ***
New dataset will be stored to database
    Given add new dataset section was open
    When user submits new dataset
    Then dataset will be stored to database

New dataset will be added to existing dataset list
    Given add new dataset section was open
    When user submits new dataset
    Then dataset will be added to existing dataset list

Deleting dataset will show alert for conformation
    Given dataset was configured
    When user clicks dataset delete button
    Then conformation alert for dataset with information will be shown
    [Teardown]    No Operation

Delete dataset will remove dataset from database
    Given dataset was configured
    When user clicks dataset delete button
    And user confirms deleting
    Then dataset will be removed from database

Delete dataset will remove dataset from existing dataset list
    Given dataset was configured
    When user clicks dataset delete button
    And user confirms deleting
    Then dataset will be removed from existing dataset list

Deleting dataset item will show alert for conformation
    Given dataset was configured
    When user clicks dataset item delete button
    Then conformation alert for item with information will be shown

Delete dataset item will remove dataset from database
    Given dataset was configured
    When user clicks dataset item delete button
    And user confirms deleting
    Then dataset item will be removed from database
    And other dataset items will be left in database
    
Delete dataset item will remove dataset from existing dataset list
    Given dataset was configured
    When user clicks dataset item delete button
    And user confirms deleting
    Then dataset item will be removed from existing dataset list
    And other dataset items will be left in existing dataset list
