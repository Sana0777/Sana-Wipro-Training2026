*** Settings ***
Library    SeleniumLibrary
Library    Collections

*** Variables ***
@{colors}    red    green    blue
@{USERS}     admin    user
@{PWDS}      admin123    user123


*** Test Cases ***
print names using for loop
    FOR    ${name}    IN    Ram    Rani    Riya
        Log To Console    ${name}
    END
    
using for loop to print list items
    FOR    ${color}    IN    @{colors}
        Log To Console    ${color}
    END
    
using for loop with range
    FOR    ${i}    IN RANGE    1    6
        Log To Console    ${i}
    END
    
FOR Loop With Step
    FOR    ${i}    IN RANGE    0    10    2 
        Log To Console    ${i}
    END
    
FOR Loop Enumerate
    FOR    ${index}    ${value}    IN ENUMERATE    a    b    c
        Log To Console    ${index}=${value}
    END        

FOR Loop Zip
    ${len}=    Get Length    ${USERS}
    FOR    ${i}    IN RANGE    ${len}
        Log To Console    ${USERS}[${i}] / ${PWDS}[${i}]
    END

Nested FOR Loop
    FOR    ${i}    IN RANGE    1    4
        FOR    ${j}    IN RANGE    1    3
            Log To Console    i=${i}, j=${j}
        END
    END

FOR Loop With IF
    FOR    ${n}    IN RANGE    1    6
        IF    ${n} == 3
            BREAK
        END
    END

using while loop to print numbers
    ${count}=    Set Variable    1
    WHILE    ${count} <= 5
        Log To Console    ${count}
        ${count}=    Evaluate    ${count} + 1
    END
