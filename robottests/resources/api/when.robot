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
