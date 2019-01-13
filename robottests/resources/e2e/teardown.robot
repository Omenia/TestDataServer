*** Keywords ***
Browser teardown
    Close All Browsers

Delete dataset case teardown
    delete dataset    ${API_URL}    ${DATASET_NAME}  
