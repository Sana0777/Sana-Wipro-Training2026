*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=registerdata.xlsx    sheet_name=Sheet1

Test Template    Login User
Test Setup       Open Login Page
Test Teardown    Close Browser

*** Variables ***
${URL}       https://tutorialsninja.com/demo/index.php?route=account/login
${BROWSER}   firefox

*** Test Cases ***
Login_With_Excel_Data

*** Keywords ***

Open Login Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    xpath=//input[@name='email']    10s


Login User
    [Arguments]    ${firstname}    ${lastname}    ${email}    ${phone}    ${password}

    Input Text    xpath=//input[@name='email']       ${email}
    Input Text    xpath=//input[@name='password']    ${password}

    Click Button    xpath=//input[@value='Login']

    Wait Until Page Contains    My Account    20s
