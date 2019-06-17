*** Keywords ***
item status in database will be "${status}"
    verify item status    ${API_URL}    ${DATASET_NAME}    ${ITEM}    ${status}

status code 200 with datasets will be received
    verify get testdata response    ${RESPONSE}    ${ALL_DATASETS}

status code 200 with next dataset item will be received
    ${dataset_name}=    Set Variable    ${DATASET_NAME}
    ${items}=           Set Variable    &{NEXT_DATASET}[items]
    verify get testdata dataset response    ${items}[1]    ${PREVIOUS_RESPONSE}    ${RESPONSE}

status code 200 with random dataset item will be received
    Should Be Equal As Numbers    ${RESPONSE.status_code}    200
    Should Be True                ${RESPONSE.json()}[testdata]

status code "${code}" will be received
    Should Be Equal As Numbers    ${RESPONSE.status_code}    ${code}

status code "${code}" will be received with error "${error}"
    Should Be Equal As Numbers    ${RESPONSE.status_code}       ${code}
    Should Be Equal               ${RESPONSE.json()}[detail]    ${error}
