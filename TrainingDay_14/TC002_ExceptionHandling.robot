*** Test Cases ***
Try Except Example
    TRY
        Fail    Something went wrong
    EXCEPT
        Log To Console    Error handled
    FINALLY
        Log To Console    Always executed
    END
