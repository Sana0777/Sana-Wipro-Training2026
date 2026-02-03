*** Settings ***
Library    SeleniumLibrary
Suite Setup    Open Browser    http://127.0.0.1:5000    chrome
Suite Teardown    Close Browser

*** Variables ***
${URL}    http://127.0.0.1:5000

*** Test Cases ***
Register Patients
    [Template]    Register Patient
    Rama    23    Male      12345    Flu     Dr. Narula
    Rani    24    Female    76543    Cold    Dr. Saksena
    Raghu    30    Male      99999    Fever   Dr. Saksena

*** Keywords ***
Register Patient
    [Arguments]    ${name}    ${age}    ${gender}    ${contact}    ${disease}    ${doctor}
    Go To    ${URL}
    Maximize Browser Window
    Input Text    name=name    ${name}
    Input Text    name=age     ${age}
    Run Keyword If    '${gender}'=='Male'
    ...    Click Element    xpath=//input[@value='Male']
    Run Keyword If    '${gender}'=='Female'
    ...    Click Element    xpath=//input[@value='Female']
    Input Text    name=contact    ${contact}
    Input Text    name=disease    ${disease}
    Select From List By Label    name=doctor    ${doctor}
    Sleep    2s
    Click Button    Register
    Wait Until Page Contains    Patient List
    sleep    2s
