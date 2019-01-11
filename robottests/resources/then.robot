*** Keywords ***
conformation alert for ${end_of_name}
    Alert Should Be Present    ${ALERT_INFO}

dataset item will be removed from database
    verify dataset item does no exist in db    ${BASE_URL}    ${DATASET_NAME}    ${DELETED_ITEM}

dataset will be removed from database
    verify dataset does no exist in db    ${BASE_URL}    ${DATASET_NAME}    

dataset will be stored to database
    verify new dataset    ${BASE_URL}    ${DATASET_NAME}    ${DATASET_ITEMS}

other dataset items will be left in database
    verify dataset item exists in db    ${BASE_URL}    ${DATASET_NAME}    ${EXISTING_ITEM}

"${page}" page will be loaded
    Wait Until Page Contains Element     &{PAGE_ELEMENT}[${page}]
