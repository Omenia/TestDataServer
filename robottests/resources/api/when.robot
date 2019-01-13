*** Keywords ***
DELETE /testdata/<dataset> request ${end_of_name}
    ${response}=    send delete testdata dataset request    ${API_URL}    ${DATASET_NAME}
    Set Test Variable    ${RESPONSE}    ${response}

DELETE /testdata/<dataset>/<item> request ${end_of_name}
    ${response}=    send get testdata dataset item request    
    ...    ${API_URL}    ${DATASET_NAME}    ${ITEM}
    Set Test Variable    ${RESPONSE}    ${response}

GET /testdata/<dataset> request ${end_of_name}
    ${response}=    send get testdata dataset request    ${API_URL}    ${DATASET_NAME}
    Set Test Variable    ${RESPONSE}    ${response}

GET "${endpoint}" request ${end_of_name}
    ${response}=    send get request    ${API_URL}    ${endpoint}   
    Set Test Variable    ${RESPONSE}    ${response}

POST /testdata request ${end_of_name}
    ${response}=    send post testdata request    ${API_URL}    ${PARAMS}   
    Set Test Variable    ${RESPONSE}    ${response}
