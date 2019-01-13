*** Keywords ***
dataset item was requested
    ${response}=    send get testdata dataset request    ${API_URL}    ${DATASET_NAMES}[0]
    Set Test Variable    ${PREVIOUS_RESPONSE}    ${response}

service was running
    Log    Service is already running after setup

testdata was configured
    add multiple dataset    ${API_URL}    ${DATASETS}
