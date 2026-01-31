*** Settings ***
Library    DataDriver    file=D:/Wipro Training/TrainingDay13/PracticeQuesDay13/testdata.csv    dialect=excel
Test Template    OrangeHRM Login With Excel
Test Setup       Open OrangeHRM
Test Teardown    Close OrangeHRM


*** Variables ***
${URL}       https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}   firefox

*** Test Cases ***
DDExcel_Login

*** Keywords ***
Open OrangeHRM
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    name=username    10s

OrangeHRM Login With Excel
    [Arguments]    ${username}    ${password}
    Log    Running with: ${username} | ${password}
    Input Text    name=username    ${username}
    Input Text    name=password    ${password}
    Sleep    2s
    Click Button    xpath=//button[@type='submit']
    Sleep    3s

Close OrangeHRM
    Close Browser
