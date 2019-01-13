*** Keywords ***
Set dataset variables
    [Arguments]    ${dataset_name}    ${item}
    Set Test Variable    ${DATASET_NAME}    ${dataset_name}
    Set Test Variable    ${ITEM}    ${item}
