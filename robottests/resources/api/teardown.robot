*** Keywords ***
Delete dataset case teardown
    delete datasets    ${API_URL}
    
Reset settings case teardown
    send put request    
    ...    ${API_URL}/settings    {"use_status": false, "use_quarantine": false, "timeout": "23:59:59"}
