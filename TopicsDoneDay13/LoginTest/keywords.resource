*** Settings ***
Library    CustomLibrary.py

*** Keywords ***
Connect to Server
    Connect    127.0.0.1

Close Server Connection
    Disconnect

Login User
    [Arguments]    ${login}    ${password}
    Login User Keyword    ${login}    ${password}

Verify Valid Login
    [Arguments]    ${exp_full_name}
    ${version}=    Get Server Version
    Should Not Be Empty    ${version}
    ${name}=    Get User Name
    Should Be Equal    ${name}    ${exp_full_name}
