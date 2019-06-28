*** Settings ***
Test Teardown    Reset settings case teardown
Resource         ../../resources/api/generic-resources.robot

*** Test Cases ***
GET /settings will receive status code 200
    [Setup]    Set Test Variable    ${RESERVATION_TIMEOUT}    23:59:59
    Given service was running
    When GET "/settings" request is send
    Then status code 200 with settings will be received

PUT /settings will receive status code 200
    [Setup]    set multiple test variables    
    ...    USE_STATUS=true    USE_QUARANTINE=true    TIMEOUT=01:12:23    
    Given service was running
    When PUT /settings request is send
    Then status code "200" will be received

Wrong use_status datatype - PUT /settings will received status code 400
    [Setup]    set multiple test variables    
    ...    USE_STATUS="true"    USE_QUARANTINE=true    TIMEOUT=01:12:23    
    Given service was running
    When PUT /settings request is send
    Then status code "400" will be received with error "'true' is not of type 'boolean'"

Wrong use_quarantine datatype - PUT /settings will received status code 400
    [Setup]    set multiple test variables    
    ...    USE_STATUS=true    USE_QUARANTINE="true"    TIMEOUT=01:12:23    
    Given service was running
    When PUT /settings request is send
    Then status code "400" will be received with error "'true' is not of type 'boolean'"

Timeout syntax error - PUT /settings will received status code 400
    [Setup]    set multiple test variables    
    ...    USE_STATUS=true    USE_QUARANTINE=true    TIMEOUT=01:12    
    Given service was running
    When PUT /settings request is send
    Then status code "400" will be received with error "Incorrect timeout syntax"
