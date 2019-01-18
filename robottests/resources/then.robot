*** Keywords ***
dataset will be stored to database
    verify new dataset    ${BASE_URL}    ${DATASET_NAME}    ${DATASET_ITEMS}

"${page}" page will be loaded
    Wait Until Page Contains Element     &{PAGE_ELEMENT}[${page}]
