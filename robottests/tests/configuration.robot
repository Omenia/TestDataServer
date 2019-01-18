*** Settings ***
Resource    ../resources/generic-resources.robot

*** Test Cases ***
New dataset will be stored to database
    Given user was on "configuration page"
    When user submits new dataset
    Then dataset will be stored to database
