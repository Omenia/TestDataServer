*** Keywords ***
user clicks add item icon
    ${locator}=    Set Variable    &{ADD_NEW_ITEM}[add-icon]
    Click Element    ${locator.format(dataset='${DATASET_NAME}')}
    Wait Until Element Is Visible    &{ADD_NEW_ITEM}[input]

user clicks dataset
    Click Element    xpath=//*[contains(text(), '${DATASET_NAME}')]
    ${locator}=    Set Variable    &{CONFIGURATION_PAGE}[dataset-item]
    Wait Until Element Is Visible    ${locator.format(dataset='${DATASET_NAME}')}

user clicks dataset delete button
    Set Test Variable    ${ACTION}    dataset-deleted
    Wait Until Element Is Visible    css=.ta-delete-${DATASET_NAME}
    Click Element    css=.ta-delete-${DATASET_NAME}
    Set Test Variable    ${ALERT_INFO}    &{ALERT_TEXT}[delete-dataset] ${DATASET_NAME}

user clicks dataset item delete button
    Set Test Variable    ${ACTION}    item-deleted
    Set Test Variable    ${DELETED_ITEM}     ${ITEMS}[0]
    Set Test Variable    ${EXISTING_ITEM}    ${ITEMS}[1]
    Wait Until Page Contains    ${DATASET_NAME}
    Click Element    css=.ta-name-${DATASET_NAME}
    Wait Until Element Is Visible    css=.ta-delete-${DATASET_NAME}-0
    Click Element    css=.ta-delete-${DATASET_NAME}-0
    Set Test Variable    ${ALERT_INFO}    &{ALERT_TEXT}[delete-item] ${DATASET_NAME} - ${DELETED_ITEM}

user clicks "${link}" navigation item
    Click Link    &{NAV_LINK}[${link}]

user confirms deleting
    Alert Should Be Present

user goes to root domain
    Go To     ${BASE_URL}

user submits new "${datatype}" dataset
    Set Test Variable    ${ACTION}    dataset-added
    Set Test Variable    ${DATASET_ITEMS}    ${ITEMS}[0]\n${ITEMS}[1]
    Input Text    &{ADD_NEW_DATASET}[name]    ${DATASET_NAME}
    Select From List By Value    &{ADD_NEW_DATASET}[datatype]    ${datatype}
    Input Text    &{ADD_NEW_DATASET}[items]    ${DATASET_ITEMS}
    Click Button    &{ADD_NEW_DATASET}[submit]
    Wait Until Element Does Not Contain    &{ADD_NEW_DATASET}[name]    ${DATASET_NAME} 

user submits new item
    Input Text    &{ADD_NEW_ITEM}[input]    ${NEW_ITEM}    
    Click Button    &{ADD_NEW_ITEM}[submit]
    Wait Until Element Is Not Visible    &{ADD_NEW_ITEM}[submit]
