*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=testdata.xlsx    sheet_name=Sheet1

Test Template    OrangeHRM Login With Excel
Test Setup       Open OrangeHRM
Test Teardown    Close Browser

*** Variables ***
${url}      https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}  firefox

*** Test Cases ***
DDExcel_Login

*** Keywords ***
Open OrangeHRM
    Open Browser    ${url}    ${browser}
    Maximize Browser Window

OrangeHRM Login With Excel
    [Arguments]    ${username}    ${password}
    Input Text    name=username    ${username}
    Input Text    name=password    ${password}
    Sleep    2s
    Click Button    xpath=//button[@type='submit']
    sleep    2s
