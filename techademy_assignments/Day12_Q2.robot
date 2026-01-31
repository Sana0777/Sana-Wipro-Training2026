*** Settings ***
Library    BuiltIn

*** Test Cases ***
Verify Environment Setup
    ${python}=    Run Process    python    --version    stdout=TRUE    shell=True
    Should Contain    ${python.stdout}    Python

    ${robot}=    Run Process    robot    --version    stdout=TRUE    shell=True
    Should Contain    ${robot.stdout}    Robot Framework

    Run Keyword And Expect Error    *    Import Library    SeleniumLibrary

    ${version}=    Get Library Version    BuiltIn
    Log To Console    Robot Framework version: ${version}
