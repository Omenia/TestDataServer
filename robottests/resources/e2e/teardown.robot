*** Keywords ***
Browser teardown
    Close All Browsers

Delete dataset case teardown
    delete datasets    ${API_URL}
    Sleep    0.1    reason=To prevent next case to be started too soon
