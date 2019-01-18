*** Keywords ***
dataset item was requested
    ${response}=    send get request    ${API_URL}/testdata/${DATASET_NAMES}[0]
    Set Test Variable    ${PREVIOUS_RESPONSE}    ${response}

service was running
    Log    Service is already running after setup

testdata was configured
    add multiple dataset    ${API_URL}    ${DATASETS}
