*** Keywords ***
user clicks "${link}" navigation item
    Click Link    &{NAV_LINK}[${link}]

user goes to root domain
    Go To     ${BASE_URL}

