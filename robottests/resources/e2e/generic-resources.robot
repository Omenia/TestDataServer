*** Settings ***
Variables    aliases.py
Resource     given.robot
Resource     when.robot
Resource     then.robot
Resource     setup.robot
Resource     teardown.robot
Library      SeleniumLibrary
Library      lib.testdata_api_client.TestdataApi
Library      lib.verify.Verify

*** Variables ***
${BROWSER}=     headlessfirefox
${BASE_URL}=    http://localhost
${API_URL}=     ${BASE_URL}/api/v1
