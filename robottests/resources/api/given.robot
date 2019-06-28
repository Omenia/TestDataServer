*** Keywords ***
all items were out of use
    ${response}=    send put request    ${API_URL}/testdata/${DATASET_NAME}/@{ITEMS}[0]    {"status": "out of use"}
    Should Be Equal As Numbers    ${response.status_code}    201
    ${response}=    send put request    ${API_URL}/testdata/${DATASET_NAME}/@{ITEMS}[1]    {"status": "out of use"}
    Should Be Equal As Numbers    ${response.status_code}    201

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
    add dataset    ${API_URL}                     &{NEXT_DATASET}[dataset]
    ...            &{NEXT_DATASET}[datatype]      &{NEXT_DATASET}[items]
    add dataset    ${API_URL}                     &{RANDOM_DATASET}[dataset]
    ...            &{RANDOM_DATASET}[datatype]    &{RANDOM_DATASET}[items]
