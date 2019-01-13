*** Keywords ***
status code 200 with datasets will be received
    verify get testdata response    ${RESPONSE}    ${DATASETS}

status code 200 with next dataset item will be received
    ${dataset_name}=    Set Variable    ${DATASET_NAMES}[0]
    ${items}=           Set Variable    &{DATASETS}[${dataset_name}]
    verify get testdata dataset response    ${items}[1]    ${PREVIOUS_RESPONSE}    ${RESPONSE}

status code "${code}" will be received
    Should Be Equal As Numbers    ${RESPONSE.status_code}    ${code}

status code "${code}" will be received with error "${error}"
    Should Be Equal As Numbers    ${RESPONSE.status_code}       ${code}
    Should Be Equal               ${RESPONSE.json()}[detail]    ${error}
