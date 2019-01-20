*** Keywords ***
Browser teardown
    Close All Browsers

Delete dataset case teardown
    delete datasets    ${API_URL}
