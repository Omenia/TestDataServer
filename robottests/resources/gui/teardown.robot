*** Keywords ***
Browser teardown
    Close All Browsers

Delete dataset case teardown
    delete datasets    ${API_URL}
    Sleep    0.1    reason=To prevent next case to be started too soon

Settings page case teardown
    Unselect Checkbox    &{${PAGE}}[use-status]
    Unselect Checkbox    &{${PAGE}}[use-quarantine]
    send put request    
    ...    ${API_URL}/settings    {"use_status": false, "use_quarantine": false, "timeout": "23:59:59"}
