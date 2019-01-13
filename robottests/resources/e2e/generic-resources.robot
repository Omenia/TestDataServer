*** Settings ***
Variables    aliases.py
Resource     given.robot
Resource     when.robot
Resource     then.robot
Resource     setup.robot
Resource     teardown.robot
Library      SeleniumLibrary
Library      lib.testdata_api.TestdataApi
Library      lib.verify.Verify

*** Variables ***
${BROWSER}=     headlessfirefox
${BASE_URL}=    http://localhost:5000
${API_URL}=     http://localhost:5000/api/v1
