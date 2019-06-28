*** Keywords ***
DELETE /testdata/<dataset> request ${end_of_name}
    ${response}=    send delete request    ${API_URL}/testdata/${DATASET_NAME}
    Set Test Variable    ${RESPONSE}    ${response}

DELETE /testdata/<dataset>/<item> request ${end_of_name}
    ${response}=    send delete request    ${API_URL}/testdata/${DATASET_NAME}/${ITEM}
    Set Test Variable    ${RESPONSE}    ${response}

GET /testdata/<dataset> request ${end_of_name}
    ${response}=    send get request    ${API_URL}/testdata/${DATASET_NAME}
    Set Test Variable    ${RESPONSE}    ${response}

GET "${endpoint}" request ${end_of_name}
    ${response}=    send get request    ${API_URL}${endpoint}
    Set Test Variable    ${RESPONSE}    ${response}

POST /testdata request ${end_of_name}
    ${response}=    send post request    ${API_URL}/testdata    ${PARAMS}
    Set Test Variable    ${RESPONSE}    ${response}

POST /testdata/<dataset>/<item> request ${end_of_name}
    ${response}=    send post request    ${API_URL}/testdata/${DATASET_NAME}/${ITEM}    {}
    Set Test Variable    ${RESPONSE}    ${response}

PUT /settings request ${end_of_name}
    ${response}=    send put request    
    ...    ${API_URL}/settings    
    ...    {"use_status": ${USE_STATUS}, "use_quarantine": ${USE_QUARANTINE}, "timeout": "${TIMEOUT}"}
    Set Test Variable    ${RESPONSE}    ${response}

PUT /testdata/<dataset>/<item> with request "${status}" ${end_of_name}
    ${response}=    send put request    ${API_URL}/testdata/${DATASET_NAME}/${ITEM}    {"status": "${status}"}
    Set Test Variable    ${RESPONSE}    ${response}

timeout elapses for item reservation
    Sleep    ${TIMEOUT}    reason=To wait time to elapse
    