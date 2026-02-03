*** Test Cases ***
using if condition
    ${age}=    Set Variable    20
    IF    ${age} >= 18
        Log To Console    you are eligible to vote
    END

IF ELSE Example
    ${num}=    Set Variable    5
    IF    ${num} > 10
        Log To Console    Greater than 10
    ELSE
        Log To Console    Less than or equal to 10
    END

IF ELSE IF Example
    ${marks}=    Set Variable    75
    IF    ${marks} >= 90
        Log To Console        Grade A
    ELSE IF    ${marks} >= 75
        Log To Console        Grade B
    ELSE
        Log To Console        Grade C
    END

Inline IF Example
    ${status}=    Set Variable    PASS
    IF    '${status}' == 'PASS'    Log To Console    Test Passed
