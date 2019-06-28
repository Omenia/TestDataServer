*** Keywords ***
user clicks add item icon
    ${locator}=    Set Variable    &{ADD_NEW_ITEM}[add-icon]
    Click Element    ${locator.format(dataset='${DATASET_NAME}')}
    Wait Until Element Is Visible    &{ADD_NEW_ITEM}[input]

user clicks dataset
    ${locator}=    Set Variable    &{EXISTING_DATASETS}[dataset-text]
    Click Element    ${locator.format(dataset='${DATASET_NAME}')}
    ${locator}=    Set Variable    &{EXISTING_DATASETS}[dataset-row]
    Wait Until Element Is Visible    ${locator.format(dataset='${DATASET_NAME}', index=0)}

user clicks dataset delete button
    Set Test Variable    ${@WHEN_ACTION}    dataset-deleted
    ${locator}=    Set Variable    &{EXISTING_DATASETS}[delete-dataset]
    Wait Until Element Is Visible    ${locator.format(dataset='${DATASET_NAME}')}
    Click Element    ${locator.format(dataset='${DATASET_NAME}')}
    Set Test Variable    ${ALERT_INFO}    &{ALERT_TEXT}[delete-dataset] ${DATASET_NAME}

user clicks dataset item delete button
    Set Test Variable    ${@WHEN_ACTION}    item-deleted
    Wait Until Page Contains    ${DATASET_NAME}
    ${locator}=    Set Variable    &{EXISTING_DATASETS}[dataset-text]
    Click Element    ${locator.format(dataset='${DATASET_NAME}')}
    ${locator}=    Set Variable    &{EXISTING_DATASETS}[delete-item]
    Wait Until Element Is Visible    ${locator.format(dataset='${DATASET_NAME}', index=0)}
    Click Element    ${locator.format(dataset='${DATASET_NAME}', index=0)}
    Set Test Variable    ${ALERT_INFO}    &{ALERT_TEXT}[delete-item] ${DATASET_NAME} - ${DELETED_ITEM}

user clicks item "${button}" button
    ${locator}=    Set Variable    &{EXISTING_DATASETS}[${button}-icon]
    Wait Until Element Is Visible    ${locator.format(dataset='${DATASET_NAME}', index=0)}
    Click Element    ${locator.format(dataset='${DATASET_NAME}', index=0)}

user clicks save button
    Set Test Variable    ${@WHEN_ACTION}    settings-saved
    Click Element    &{SETTINGS_PAGE}[save-settings]

user clicks "${link}" navigation item
    Click Link    &{NAV_LINK}[${link}]

user confirms deleting
    Alert Should Be Present

user goes to root domain
    Go To     ${BASE_URL}

user selects "${checkbox}" checkbox
    Select Checkbox    &{${PAGE}}[${checkbox.replace(' ', '-')}]

user submits new "${datatype}" dataset
    Set Test Variable    ${@WHEN_ACTION}    dataset-added
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

user unselects "${checkbox}" checkbox
    Unselect Checkbox    &{${PAGE}}[${checkbox.replace(' ', '-')}]

user visits dashboard page
    Go To    ${BASE_URL}&{ON_PAGE}[dashboard page]
