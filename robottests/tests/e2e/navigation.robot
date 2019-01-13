*** Settings ***
Resource    ../../resources/e2e/generic-resources.robot

*** Test Cases ***
Dashboard will be landing page
    Given user was not on "the site"
    When user goes to root domain
    Then "dashboard" page will be loaded

Dashboard navigation link will transfer to dashboard page
    Given user was not on "dashboard page"
    When user clicks "dashboard" navigation item
    Then "dashboard" page will be loaded

Configuration navigation link will transfer to configuration page
    Given user was not on "configuration page"
    When user clicks "configuration" navigation item
    Then "configuration" page will be loaded

Swagger navigation link will transfer to Swagger page
    Given user was not on "Swagger page"
    When user clicks "Swagger" navigation item
    Then "Swagger" page will be loaded
