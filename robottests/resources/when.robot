*** Keywords ***
user clicks dataset delete button
    Wait Until Element Is Visible    css=.ta_delete_${DATASET_NAME}
    Click Element    css=.ta_delete_${DATASET_NAME}
    Set Test Variable    ${ALERT_INFO}    &{ALERT_TEXT}[delete-dataset] ${DATASET_NAME}

user clicks dataset item delete button
    Set Test Variable    ${DELETED_ITEM}     ${ITEMS}[0]
    Set Test Variable    ${EXISTING_ITEM}    ${ITEMS}[1]
    Wait Until Page Contains    ${DATASET_NAME}
    Click Element    css=.ta_name_${DATASET_NAME}
    Wait Until Element Is Visible    css=.ta_delete_${DATASET_NAME}_0
    Click Element    css=.ta_delete_${DATASET_NAME}_0
    Set Test Variable    ${ALERT_INFO}    &{ALERT_TEXT}[delete-item] ${DATASET_NAME} - ${DELETED_ITEM}

user clicks "${link}" navigation item
    Click Link    &{NAV_LINK}[${link}]

user confirms deleting
    Alert Should Be Present

user goes to root domain
    Go To     ${BASE_URL}

user submits new dataset
    Set Test Variable    ${DATASET_ITEMS}    ${ITEMS}[0]\n${ITEMS}[1]
    Input Text    &{NEW_DATASET_FORM}[name]    ${DATASET_NAME}
    Input Text    &{NEW_DATASET_FORM}[items]    ${DATASET_ITEMS}
    Click Button    &{NEW_DATASET_FORM}[submit]
    Wait Until Element Does Not Contain    &{NEW_DATASET_FORM}[name]    ${DATASET_NAME} 
