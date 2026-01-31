*** Settings ***
Library    BuiltIn

*** Variables ***
${SCALAR_VAR}    Hello Robot
@{LIST_VAR}      Apple    Banana    Cherry

*** Test Cases ***
Test Case 1 - Log Messages
    Log    This is a normal log message
    Log To Console    This message will appear in the console
    Log    Scalar variable value is: ${SCALAR_VAR}
    Log    List variable values are: @{LIST_VAR}

Test Case 2 - Use Variables
    ${first_item}=    Set Variable    ${LIST_VAR}[0]
    Log    First item in the list is: ${first_item}
    ${second_item}=    Set Variable    ${LIST_VAR}[1]
    Log To Console    Second item in the list is: ${second_item}
