*** Keywords ***
"${page}" page will be loaded
    Wait Until Element Contains     &{PAGE_HEADER_ELEMENT}[${page}]    &{PAGE_HEADER_TEXT}[${page}]
