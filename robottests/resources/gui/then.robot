*** Keywords ***
add item container will be hidden
    Wait Until Element Is Not Visible    &{ADD_NEW_DATASET}[submit]

button will be changed to "${button}"
    ${locator}=    Set Variable    &{EXISTING_DATASETS}[${button}-icon]
    Wait Until Element Is Visible    ${locator.format(dataset='${DATASET_NAME}', index=0)}

conformation alert for ${end_of_name}
    Alert Should Be Present    ${ALERT_INFO}

dataset item will be removed from database
    Sleep    0.1    reason=To prevent verification to be done too soon
    verify dataset item does no exist in db    ${API_URL}    ${DATASET_NAME}    ${DELETED_ITEM}

dataset item will be removed from existing dataset list
    Wait Until Page Does Not Contain    ${DELETED_ITEM}

dataset item will be stored to database
    verify new dataset    ${API_URL}    ${DATASET_NAME}    ${ITEMS}[0]\n${ITEMS}[1]\n${NEW_ITEM}

dataset will be added to existing dataset list
    ${locator}=    Set Variable    &{EXISTING_DATASETS}[dataset-row]
    Wait Until Element Contains    ${locator.format(dataset='${DATASET_NAME}')}    ${DATASET_NAME}

dataset will be removed from database
    Sleep    0.1    reason=To prevent verification to be done too soon
    verify dataset does no exist in db    ${API_URL}    ${DATASET_NAME}    

dataset will be removed from existing dataset list
    ${locator}=    Set Variable    &{EXISTING_DATASETS}[dataset-row]
    Wait Until Page Does Not Contain Element    ${locator.format(dataset='${DATASET_NAME}')}

dataset will be shown in dashboard
    ${locator}=    Set Variable    &{DASHBOARD_PAGE}[dataset]
    Wait Until Page Contains Element    ${locator.format(dataset_name='${DATASET_NAME}')}
    verify dataset in dashboard    ${DATASET_NAME}    ${ITEMS}    ${STATUS}

dataset will be stored to database
    verify new dataset    ${API_URL}    ${DATASET_NAME}    ${DATASET_ITEMS}

item will be added to existing dataset item list
    Wait Until Page Contains    ${NEW_ITEM}

item will be set as available
    ${locator}=    Set Variable    &{EXISTING_DATASETS}[item-status]
    Wait Until Page Does Not Contain    ${locator.format(dataset='${DATASET_NAME}', index=0)}

item will be set as out of use
    Wait Until Element Contains    css=.ta-status-${DATASET_NAME}-0    out of use

notification will be hidden
    Wait Until Page Does Not Contain    ${SHOWN_INFO_TEXT}         timeout=7
    Page Should Contain Element         &{INFO_ELEMENT}[hidden] 

notification will stay visible
    Sleep    7    reason=Waiting to check later that notification is still visible
    Page Should Contain Element    &{INFO_ELEMENT}[error] 
    Page Should Contain            ${SHOWN_INFO_TEXT}

other dataset items will be left in database
    Sleep    0.1    reason=To prevent verification to be done too soon
    verify dataset item exists in db    ${API_URL}    ${DATASET_NAME}    ${EXISTING_ITEM}

other dataset items will be left in existing dataset list
    Page Should Contain    ${EXISTING_ITEM}

"${element}" ${_} will be disabled
    Element Should Be Disabled    &{${PAGE}}[${element.replace(' ', '-')}]

"${element}" ${_} will be enabled
    Element Should Be Enabled    &{${PAGE}}[${element.replace(' ', '-')}]

"${status}" notification will be shown
    Set Test Variable    ${SHOWN_INFO_TEXT}     &{INFO_TEXT}[${@WHEN_ACTION}-${status}]
    Wait Until Page Contains Element    &{INFO_ELEMENT}[${status}]
    Wait Until Page Contains            ${SHOWN_INFO_TEXT}

"${page}" page will be loaded
    Wait Until Page Contains Element     &{PAGE_ELEMENT}[${page}]
