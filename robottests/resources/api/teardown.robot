*** Keywords ***
Delete dataset case teardown
    delete multiple dataset    ${API_URL}    ${DATASET_NAMES}  
