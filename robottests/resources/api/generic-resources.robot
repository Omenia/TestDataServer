*** Settings ***
# Variables    aliases.py
Resource     given.robot
Resource     when.robot
Resource     then.robot
Resource     setup.robot
Resource     teardown.robot
Library      lib.testdata_api.TestdataApi
Library      lib.verify.Verify

*** Variables ***
${API_URL}=    http://localhost:5000/api/v1
