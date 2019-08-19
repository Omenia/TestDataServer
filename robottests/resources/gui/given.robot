*** Keywords ***
add item container was visible
    ${locator}=    Set Variable    &{ADD_NEW_ITEM}[add-icon]
    Click Element    ${locator.format(dataset='${DATASET_NAME}')}
    Wait Until Element Is Visible    &{ADD_NEW_ITEM}[input]

add new dataset section was open
    Go To    ${BASE_URL}&{ON_PAGE}[configuration page]
    Click Element    &{ADD_NEW_DATASET}[header]
    Wait Until Element Is Visible    &{ADD_NEW_DATASET}[submit]

dataset section was open
    "${DATATYPE}" dataset was configured
    ${locator}=    Set Variable    &{EXISTING_DATASETS}[dataset-text]
    Click Element    ${locator.format(dataset='${DATASET_NAME}')}
    ${locator}=    Set Variable    &{EXISTING_DATASETS}[dataset-row]
    Wait Until Element Is Visible    ${locator.format(dataset='${DATASET_NAME}', index=0)}

item was out of use
    ${locator}=    Set Variable    &{EXISTING_DATASETS}[stop-icon]
    Wait Until Element Is Visible    ${locator.format(dataset='${DATASET_NAME}', index=0)}
    Click Element    ${locator.format(dataset='${DATASET_NAME}', index=0)}
    
settings were set
    use quarantine checkbox was selected
    Input Text    &{SETTINGS_PAGE}[timeout]    ${RESERVATION_TIMEOUT}

use quarantine checkbox was enabled
    Select Checkbox    &{SETTINGS_PAGE}[use-status]
    Element Should Be Enabled    &{SETTINGS_PAGE}[use-quarantine]

use quarantine checkbox was selected
    Use quarantine checkbox was enabled
    Select Checkbox    &{SETTINGS_PAGE}[use-quarantine]

user was not on "${page}"
    Go To    ${BASE_URL}&{NOT_ON_PAGE}[${page}]

user was on "${page}"
    Go To    ${BASE_URL}&{ON_PAGE}[${page}]

"${datatype}" dataset was configured
    add dataset    ${API_URL}
    ...    {"dataset": "${DATASET_NAME}", "items": [${ITEMS}[0], ${ITEMS}[1]], "datatype": "${datatype}"}
    Go To    ${BASE_URL}&{ON_PAGE}[configuration page]
    Wait Until Page Contains    ${DATASET_NAME}

"${checkbox}" checkbox was selected
    Select Checkbox    &{${PAGE}}[${checkbox.replace(' ', '-')}]

"${checkbox}" checkbox was unselected
    Checkbox Should Not Be Selected    &{${PAGE}}[${checkbox.replace(' ', '-')}]

"${element}" ${_} was enabled
    Element Should Be Enabled    &{${PAGE}}[${element.replace(' ', '-')}]
