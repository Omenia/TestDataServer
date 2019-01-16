*** Keywords ***
conformation alert for ${end_of_name}
    Alert Should Be Present    ${ALERT_INFO}

dataset item will be removed from database
    verify dataset item does no exist in db    ${API_URL}    ${DATASET_NAME}    ${DELETED_ITEM}

dataset will be removed from database
    verify dataset does no exist in db    ${API_URL}    ${DATASET_NAME}    

dataset will be stored to database
    verify new dataset    ${API_URL}    ${DATASET_NAME}    ${DATASET_ITEMS}

notification will be hidden
    Wait Until Page Does Not Contain    ${SHOWN_INFO_TEXT}         timeout=7
    Page Should Contain Element         &{INFO_ELEMENT}[hidden] 

notification will stay visible
    Sleep    7    reason=Waiting to check later that notification is still visible
    Page Should Contain Element    &{INFO_ELEMENT}[error] 
    Page Should Contain            ${SHOWN_INFO_TEXT}

other dataset items will be left in database
    verify dataset item exists in db    ${API_URL}    ${DATASET_NAME}    ${EXISTING_ITEM}

"${status}" notification will be shown
    Set Test Variable    ${SHOWN_INFO_TEXT}     &{INFO_TEXT}[${ACTION}-${status}]
    Wait Until Page Contains Element    &{INFO_ELEMENT}[${status}]
    Wait Until Page Contains            ${SHOWN_INFO_TEXT}

"${page}" page will be loaded
    Wait Until Page Contains Element     &{PAGE_ELEMENT}[${page}]
