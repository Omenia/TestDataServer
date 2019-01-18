*** Keywords ***
user was not on "${page}"
    Go To    ${BASE_URL}&{NOT_ON_PAGE}[${page}]

user was on "${page}"
    Go To    ${BASE_URL}&{ON_PAGE}[${page}]
