*** Settings ***
Test Teardown    Delete dataset case teardown
Resource         ../../resources/e2e/generic-resources.robot

*** Variables ***
${DATASET_NAME}    dataset-1
@{ITEMS}           {"key-a1": "value-a1", "key-a2": "value-a2"}
...                {"key-b1": "value-b1", "key-b2": "value-b2"}

*** Test Cases ***
Add new dataset - Ok - Notification will be shown
    Given add new dataset section was open
    When user submits new dataset
    Then "ok" notification will be shown

Add new dataset - Error - Notification will be shown
    Given dataset was configured
    And add new dataset section was open
    When user submits new dataset
    Then "error" notification will be shown

Delete dataset - Ok - Notification will be shown
    Given dataset was configured
    When user clicks dataset delete button
    And user confirms deleting
    Then "ok" notification will be shown

Delete item - Ok - Notification will be shown
    Given dataset was configured
    When user clicks dataset item delete button
    And user confirms deleting
    Then "ok" notification will be shown
    
Ok notification will be shown and hidden
    Given add new dataset section was open
    When user submits new dataset
    Then "ok" notification will be shown
    And notification will be hidden

Error notification will be shown and not hidden
    Given dataset was configured
    And add new dataset section was open
    When user submits new dataset
    Then "error" notification will be shown
    And notification will stay visible
