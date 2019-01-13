*** Settings ***
Resource         ../../resources/api/generic-resources.robot

*** Test Cases ***
GET /status will receive status code 200
    Given service was running
    When GET "/status" request is send
    Then status code "200" will be received
