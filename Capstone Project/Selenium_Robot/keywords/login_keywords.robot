*** Settings ***
Library        SeleniumLibrary
Resource    ../resources/config.robot
Resource    ../resources/locators.robot
Resource    common_keywords.robot

*** Keywords ***
Login As User
    [Documentation]    Full login flow with assertions at every step.
    [Arguments]    ${email}    ${password}

    Log    STEP 3: LOGIN ${email}    INFO

    Click Element    ${LOC_LOGIN_LINK}
    Assert URL Contains    login
    ${title}=    Get Title
    Should Contain    ${title}    Login
    ...    msg=Expected 'Login' in page title, got '${title}'

    Assert Element Visible    ${LOC_LOGIN_EMAIL}      Email field not visible
    Assert Element Visible    ${LOC_LOGIN_PASSWORD}   Password field not visible
    Assert Element Visible    ${LOC_LOGIN_BTN}        Login button not visible

    Input Text      ${LOC_LOGIN_EMAIL}      ${email}
    Element Attribute Value Should Be    ${LOC_LOGIN_EMAIL}    value    ${email}
    Input Password  ${LOC_LOGIN_PASSWORD}   ${password}
    Click Element   ${LOC_LOGIN_BTN}

    Wait Until Element Is Visible    ${LOC_ACCOUNT_LINK}    timeout=${EXPLICIT_WAIT}
    ...    error=Account link not visible after login — login may have failed for '${email}'
    ${account}=    Get Text    ${LOC_ACCOUNT_LINK}
    Should Not Be Empty    ${account}    msg=Logged-in account text is empty

    # demowebshop sometimes shows "My account" instead of email — both confirm login succeeded
    ${email_lower}=      Convert To Lower Case    ${email}
    ${account_lower}=    Convert To Lower Case    ${account}
    ${contains_email}=   Run Keyword And Return Status
    ...    Should Contain    ${account_lower}    ${email_lower}
    IF    not ${contains_email}
        Log    Account shows '${account}' instead of email — login still confirmed    WARN
    END

    ${url}=    Get Location
    Should Not Contain    ${url}    login
    ...    msg=Still on login page after login: ${url}

    Log    Logged in — account link shows: '${account}'    INFO

Logout User
    [Documentation]    Logout via direct /logout URL.
    Log    STEP 10: LOGOUT    INFO
    ${is_logged_in}=    Run Keyword And Return Status
    ...    Element Should Be Visible    ${LOC_ACCOUNT_LINK}
    IF    not ${is_logged_in}
        Log    No active session found — skipping logout    WARN
        RETURN
    END
    Go To    ${BASE_URL}/logout
    Sleep    1s
    Log    Logout successful    INFO

Verify Session Terminated
    [Documentation]    Navigate to a protected page and assert redirect to login.
    Log    STEP 11: VERIFY SESSION TERMINATED    INFO
    Go To    ${BASE_URL}/customer/info
    Sleep    2s
    Assert URL Contains    login
    Log    Session confirmed terminated    INFO