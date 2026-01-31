*** Settings ***
Library    SeleniumLibrary
Library    RPA.Tables
Suite Setup    Open Browser To OrangeHRM
Suite Teardown    Close Browser

*** Variables ***
${CSV_FILE}    testdata1.csv

*** Test Cases ***
Login Data-Driven From CSV
    ${data}=    Read CSV File    ${CSV_FILE}
    :FOR    ${row}    IN    @{data}
    \    Login Test Template    ${row['username']}    ${row['password']}    ${row['expected']}

*** Keywords ***
Open Browser To OrangeHRM
    Open Browser    https://opensource-demo.orangehrmlive.com/    chrome
    Maximize Browser Window

Close Browser
    Close Browser

Login With Credentials
    [Arguments]    ${username}    ${password}
    Input Text     id=txtUsername    ${username}
    Input Text     id=txtPassword    ${password}
    Click Button   id=btnLogin

Verify Login Successful
    Page Should Contain    Dashboard

Verify Login Failed
    Page Should Contain    Invalid credentials

Login Test Template
    [Arguments]    ${username}    ${password}    ${expected}
    Login With Credentials    ${username}    ${password}
    Run Keyword If    '${expected}'=='Pass'    Verify Login Successful
    ...               ELSE    Verify Login Failed
