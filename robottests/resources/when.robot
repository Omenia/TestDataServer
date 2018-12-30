*** Keywords ***
user clicks "${link}" navigation item
    Click Link    &{NAV_LINK}[${link}]

user goes to root domain
    Go To     ${BASE_URL}

user submits new dataset
    Set Test Variable    ${DATASET_NAME}    test set
    Set Test Variable    ${DATASET_ITEMS}    {"username": "user1", "password": "passwd", "email": "user1@example.com"}${\n}{"username": "user2", "password": "passwd", "email": "user2@example.com"}
    Input Text    &{NEW_DATASET_FORM}[name]    ${DATASET_NAME}
    Input Text    &{NEW_DATASET_FORM}[items]    ${DATASET_ITEMS}
    Click Button    &{NEW_DATASET_FORM}[submit]
    Wait Until Element Does Not Contain    &{NEW_DATASET_FORM}[name]    ${DATASET_NAME} 
