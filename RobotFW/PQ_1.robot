*** Settings ***
Library    BuiltIn

*** Variables ***
${Name}        Robot Framework
${Version}     7.4.1
@{Colors}       Red    Green    Blue

*** Test Cases ***

Show Basic Information
    Log    Starting first test case
    Log To Console    Hii from Robot Framework
    Log    Tool Name: ${Name}
    Log    Version: ${Version}
    Log    Available Colors: ${Colors}
    Log To Console    First test case completed

Display List Values
    Log    Starting second test case
    Log    First Color: ${Colors}[0]
    Log    Second Color: ${Colors}[1]
    Log    Third Color: ${Colors}[2]
    Log To Console    Colors displayed successfully
    Log    Second test case completed
