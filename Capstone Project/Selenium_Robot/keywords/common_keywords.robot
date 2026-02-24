*** Settings ***
Resource    ../resources/config.robot
Resource    ../resources/locators.robot

*** Keywords ***
Open Browser To Site
     [Documentation]    Open browser, go to BASE_URL, assert site loaded
    ${browser_lower}=    Convert To Lower Case    ${BROWSER}
    IF    '${browser_lower}' == 'edge' or '${browser_lower}' == 'chrome'
        ${options}=    Evaluate
        ...    sys.modules['selenium.webdriver'].EdgeOptions() if '${browser_lower}' == 'edge' else sys.modules['selenium.webdriver'].ChromeOptions()
        ...    sys
        Call Method    ${options}    add_argument    --ignore-certificate-errors
        Call Method    ${options}    add_argument    --ignore-ssl-errors
        Call Method    ${options}    add_argument    --allow-insecure-localhost
        Call Method    ${options}    add_argument    --no-first-run
        Call Method    ${options}    add_argument    --no-default-browser-check

        Open Browser    ${BASE_URL}    ${BROWSER}    options=${options}
    ELSE
        Open Browser    ${BASE_URL}    ${BROWSER}
    END
    Maximize Browser Window
    Set Selenium Implicit Wait    ${IMPLICIT_WAIT}
    ${title}=    Get Title
    Should Not Be Empty    ${title}    msg=Page title empty – site may not have loaded
    Log    Browser opened at ${BASE_URL} | Title: ${title}

Close Browser Session
    [Documentation]    Close the browser
    Close Browser
    Log    Browser session closed

Assert URL Contains
    [Documentation]    Fail if current URL does not contain the expected fragment
    [Arguments]    ${fragment}
    ${url}=    Get Location
    Should Contain    ${url}    ${fragment}
    ...    msg=URL '${url}' does not contain expected fragment '${fragment}'

Assert Element Visible
    [Arguments]    ${locator}    ${message}=Element not visible
    Wait Until Element Is Visible    ${locator}    timeout=${EXPLICIT_WAIT}
    ...    error=${message}

Assert Text Contains
    [Arguments]    ${locator}    ${expected}
    ${text}=    Get Text    ${locator}
    Should Contain    ${text}    ${expected}
    ...    msg=Expected '${expected}' in text but got '${text}'
    RETURN    ${text}