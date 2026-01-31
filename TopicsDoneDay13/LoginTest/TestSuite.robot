*** Settings ***
Documentation     A test suite for valid login.
Resource          keywords.resource
Default Tags      positive

*** Test Cases ***
Login User with Password
    Connect to Server
    Login User    ironman    1234567890
    Verify Valid Login    Tony Stark
    [Teardown]    Close Server Connection

Denied Login with Wrong Password
    [Tags]    negative
    Connect to Server
    Run Keyword And Expect Error    *Invalid Password    Login User    ironman    123
    [Teardown]    Close Server Connection
