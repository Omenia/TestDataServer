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
    Click Element    xpath=//*[contains(text(), '${DATASET_NAME}')]
    ${locator}=    Set Variable    &{CONFIGURATION_PAGE}[dataset-item]
    Wait Until Element Is Visible    ${locator.format(dataset='${DATASET_NAME}', index=0)}

item was out of use
    Wait Until Element Is Visible    css=.ta-stop-${DATASET_NAME}-0
    Click Element    css=.ta-stop-${DATASET_NAME}-0

user was not on "${page}"
    Go To    ${BASE_URL}&{NOT_ON_PAGE}[${page}]

user was on "${page}"
    Go To    ${BASE_URL}&{ON_PAGE}[${page}]

"${datatype}" dataset was configured
    add dataset    ${API_URL}    ${DATASET_NAME}    ${datatype}    ${ITEMS}
    Go To    ${BASE_URL}&{ON_PAGE}[configuration page]
    Wait Until Page Contains    ${DATASET_NAME}
