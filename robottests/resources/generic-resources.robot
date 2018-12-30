*** Settings ***
Variables    aliases.py
Resource     given.robot
Resource     when.robot
Resource     then.robot
Resource     setup.robot
Resource     teardown.robot
Library      SeleniumLibrary
Library      lib.verify.Verify

*** Variables ***
${BROWSER}=    headlessfirefox
${BASE_URL}=    http://localhost:5000