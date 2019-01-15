*** Settings ***
Suite Setup      Browser setup
Suite Teardown    Browser teardown
Resource         ../resources/generic-resources.robot

*** Variables ***
${BROWSER}=    headlessfirefox
${BASE_URL}=    http://localhost:5000

*** Test Cases ***
Dashboard will be landing page
    Given user was not on "the site"
    When user goes to root domain
    Then "dashboard" page will be loaded

Swagger navigation link will transfer to Swagger page
    Given user was not on "Swagger page"
    When user clicks "Swagger" navigation item
    Then "Swagger" page will be loaded
