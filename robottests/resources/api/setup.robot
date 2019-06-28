*** Keywords ***
Set dataset variables
    [Arguments]    ${dataset_name}    ${item}
    Set Test Variable    ${DATASET_NAME}    ${dataset_name}
    Set Test Variable    ${ITEM}    ${item}

Setup settings
    [Arguments]    ${use_status}    ${use_quarantine}    ${timeout}
    send put request    
    ...    ${API_URL}/settings    
    ...    {"use_status": ${use_status}, "use_quarantine": ${use_quarantine}, "timeout": "${timeout}"}
