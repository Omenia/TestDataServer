*** Keywords ***
user was not on "${page}"
    Go To    ${BASE_URL}&{NOT_ON_PAGE}[${page}]
