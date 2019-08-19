*** Keywords ***
all items were out of use
    ${response}=    send put request    ${API_URL}/testdata/${DATASET_NAME}/@{ITEMS}[0]    {"status": "out of use"}
    Should Be Equal As Numbers    ${response.status_code}    200
    ${response}=    send put request    ${API_URL}/testdata/${DATASET_NAME}/@{ITEMS}[1]    {"status": "out of use"}
    Should Be Equal As Numbers    ${response.status_code}    200

dataset item was requested
    ${response}=    send get request    ${API_URL}/testdata/${DATASET_NAME}

item was reserved
    Testdata was configured
    ${response}=    send get request    ${API_URL}/testdata/${DATASET_NAME}    

oldest item was out of use
    send put request    ${API_URL}/testdata/${DATASET_NAME}/${OLDEST_ITEM}    {"status": "out of use"}
    verify item status    ${API_URL}    ${DATASET_NAME}    ${OLDEST_ITEM}    out of use

service was running
    Log    Service is already running after setup

testdata was configured
    add dataset    ${API_URL}
    ...    {"dataset": "${DATASET_NAMES}[0]", "items": [${ITEMS_0}[0], ${ITEMS_0}[1]], "datatype": "next"}
    add dataset    ${API_URL}
    ...    {"dataset": "${DATASET_NAMES}[1]", "items": [${ITEMS_1}[0], ${ITEMS_1}[1]], "datatype": "random"}
