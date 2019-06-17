*** Settings ***
# Variables    aliases.py
Resource     given.robot
Resource     when.robot
Resource     then.robot
Resource     setup.robot
Resource     teardown.robot
Library      lib.testdata_api_client.TestdataApi
Library      lib.verify.Verify
Library      lib.utils

*** Variables ***
${BASE_URL}=    http://localhost
${API_URL}=     ${BASE_URL}/api/v1
