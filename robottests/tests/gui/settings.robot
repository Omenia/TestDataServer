*** Settings ***
Suite Setup      Go To    ${BASE_URL}&{ON_PAGE}[settings page]
Test Teardown    Settings page case teardown
Resource         ../../resources/gui/generic-resources.robot

*** Variables ***
${PAGE}=    SETTINGS_PAGE

*** Test Cases ***
Selecting use status checkbox will enable use quarantine checkbox
    Given "use status" checkbox was unselected
    When user selects "use status" checkbox
    Then "use quarantine" checkbox will be enabled

Selecting use quarantine checkbox will enable timeout input
    Given use quarantine checkbox was enabled
    And "use quarantine" checkbox was unselected
    When user selects "use quarantine" checkbox
    Then "timeout" input will be enabled

Unselecting use quarantine checkbox will disable timeout input 
    Given use quarantine checkbox was selected
    And "timeout" input was enabled
    When user unselects "use quarantine" checkbox
    Then "timeout" input will be disabled

Unselecting use status checkbox will disable use quarantine checkbox
    Given "use status" checkbox was selected
    And "use quarantine" checkbox was enabled
    When user unselects "use status" checkbox
    Then "use quarantine" checkbox will be disabled
    
Valid syntax - Saving settings will shown success notification 
    [Setup]    Set Test Variable    ${RESERVATION_TIMEOUT}    11:22:33
    Given settings were set
    When user clicks save button
    Then "ok" notification will be shown

Invalid syntax - Saving settings will shown error notification 
    [Setup]    Set Test Variable    ${RESERVATION_TIMEOUT}    invalid
    Given settings were set
    When user clicks save button
    Then "error" notification will be shown    
