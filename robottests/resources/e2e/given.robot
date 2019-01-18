*** Keywords ***
add new dataset section was open
    Go To    ${BASE_URL}&{ON_PAGE}[configuration page]
    Click Element    &{ADD_NEW_DATASET}[header]
    Wait Until Element Is Visible    &{ADD_NEW_DATASET}[submit]

dataset was configured
    add dataset    ${API_URL}    ${DATASET_NAME}    @{ITEMS}    
    Go To    ${BASE_URL}&{ON_PAGE}[configuration page]

user was not on "${page}"
    Go To    ${BASE_URL}&{NOT_ON_PAGE}[${page}]

user was on "${page}"
    Go To    ${BASE_URL}&{ON_PAGE}[${page}]
