*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=registerdata.xlsx    sheet_name=Sheet1

Test Template    Register User
Test Setup       Open Registration Page
Test Teardown    Close Browser

*** Variables ***
${URL}       https://tutorialsninja.com/demo/index.php?route=account/register
${BROWSER}   firefox

*** Test Cases ***
Register_With_Excel_Data

*** Keywords ***

Open Registration Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    xpath=//input[@name='firstname']    5s


Register User
    [Arguments]    ${firstname}    ${lastname}    ${email}    ${phone}    ${password}

    Input Text    xpath=//input[@name='firstname']    ${firstname}

    Input Text    xpath=//input[@name='lastname']     ${lastname}

    Input Text    xpath=//input[@name='email']        ${email}

    Input Text    xpath=//input[@name='telephone']    ${phone}

    Input Text    xpath=//input[@name='password']     ${password}

    Input Text    xpath=//input[@name='confirm']      ${password}


    Click Element    xpath=//input[@name='newsletter' and @value='0']

    Sleep    1s

    Click Element    xpath=//input[@name='agree']

    Sleep    1s

    Click Button    xpath=//input[@value='Continue']

    Wait Until Page Contains    Your Account Has Been Created!    5s

    Log    Registration Successful for: ${email}
