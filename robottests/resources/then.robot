*** Keywords ***
"${page}" page will be loaded
    Wait Until Page Contains Element     &{PAGE_ELEMENT}[${page}]
