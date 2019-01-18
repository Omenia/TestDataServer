*** Keywords ***
Browser teardown
    Close All Browsers

Delete dataset case teardown
    delete dataset    ${BASE_URL}    ${DATASET_NAME}  
