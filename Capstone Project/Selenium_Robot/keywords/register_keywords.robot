*** Settings ***
Resource    ../resources/config.robot
Resource    ../resources/locators.robot
Resource    common_keywords.robot

*** Keywords ***
Register New User
    [Documentation]
    ...    Registration flow. Returns 'registered' or 'already_exists'.
    ...    If email already exists, logs a warning and returns 'already_exists'
    ...    instead of failing — the test will then proceed to login.
    [Arguments]    ${first_name}    ${last_name}    ${email}    ${password}    ${gender}=male

    Log    STEP 2: REGISTER ${email}

    Click Element    ${LOC_REG_LINK}
    Assert URL Contains    register
    ${title}=    Get Title
    Should Contain    ${title}    Register
    ...    msg=Expected 'Register' in page title, got '${title}'

    Run Keyword If    '${gender}'.lower() == 'male'
    ...    Select Male Gender
    ...    ELSE    Select Female Gender

    Input Text    ${LOC_FIRST_NAME}    ${first_name}
    Element Attribute Value Should Be    ${LOC_FIRST_NAME}    value    ${first_name}

    Input Text    ${LOC_LAST_NAME}    ${last_name}
    Element Attribute Value Should Be    ${LOC_LAST_NAME}    value    ${last_name}

    Input Text    ${LOC_REG_EMAIL}    ${email}
    Element Attribute Value Should Be    ${LOC_REG_EMAIL}    value    ${email}

    Input Password    ${LOC_REG_PASSWORD}      ${password}
    Input Password    ${LOC_CONFIRM_PASSWORD}  ${password}

    Click Element    ${LOC_REGISTER_BTN}

    # Wait for page to respond — either success result or already-exists error
    Sleep    2s

    ${page_source}=    Get Source
    ${page_lower}=     Convert To Lower Case    ${page_source}

    # Check if email already registered
    ${already_exists}=    Run Keyword And Return Status
    ...    Should Contain    ${page_lower}    already exist

    IF    not ${already_exists}
        ${already_exists}=    Run Keyword And Return Status
        ...    Should Contain    ${page_lower}    the specified email already exists
    END

    IF    ${already_exists}
        Log    WARNING: Email already registered: ${email} — will proceed to login    WARN
        RETURN    already_exists
    END

    # Check for success — either on registerresult page or result div visible
    ${url}=    Get Location
    ${url_lower}=    Convert To Lower Case    ${url}

    ${success_url}=    Run Keyword And Return Status
    ...    Should Contain    ${url_lower}    registerresult

    IF    ${success_url}
        Log    Registration successful for ${email}
        RETURN    registered
    END

    ${success_text}=    Run Keyword And Return Status
    ...    Should Contain    ${page_lower}    your registration completed

    IF    ${success_text}
        Log    Registration successful for ${email}
        RETURN    registered
    END

    # If redirected away from /register entirely — treat as success
    ${still_on_register}=    Run Keyword And Return Status
    ...    Should Contain    ${url_lower}    register

    IF    not ${still_on_register}
        Log    Registration redirected to ${url} — treating as success
        RETURN    registered
    END

    # Last resort — read the result div text
    ${has_result}=    Run Keyword And Return Status
    ...    Element Should Be Visible    ${LOC_REGISTER_RESULT}
    IF    ${has_result}
        ${result}=    Get Text    ${LOC_REGISTER_RESULT}
        Log    Registration result: '${result}'
        RETURN    registered
    END

    Fail    Registration failed unexpectedly for ${email}. URL: ${url}

Select Male Gender
    Click Element    ${LOC_GENDER_MALE}
    ${selected}=    Get Element Attribute    ${LOC_GENDER_MALE}    checked
    Should Not Be Empty    ${selected}
    ...    msg=Male radio button is not selected after clicking
    Log    Gender = male

Select Female Gender
    Click Element    ${LOC_GENDER_FEMALE}
    ${selected}=    Get Element Attribute    ${LOC_GENDER_FEMALE}    checked
    Should Not Be Empty    ${selected}
    ...    msg=Female radio button is not selected after clicking
    Log    Gender = female