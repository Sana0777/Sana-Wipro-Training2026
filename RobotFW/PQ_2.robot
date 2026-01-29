*** Settings ***
Library    SeleniumLibrary
Library    BuiltIn

*** Test Cases ***
Verify Automation Setup
    Verify Python
    Verify Robot
    Verify Selenium
    Log    All dependencies are ready

*** Keywords ***

Verify Python
    ${version}=    Evaluate    sys.version    modules=sys
    Run Keyword If    '${version}' == ''    Fail    Python is not installed
    Log    Python version: ${version}
    Log To Console    Python: ${version}

Verify Robot
    ${version}=    Evaluate    __import__('robot').__version__
    Run Keyword If    '${version}' == ''    Fail    Robot Framework not installed
    Log    Robot Framework version: ${version}
    Log To Console    Robot Framework: ${version}

Verify Selenium
    ${version}=    Evaluate    __import__('importlib.metadata', fromlist=['']).version('robotframework-seleniumlibrary')
    Run Keyword If    '${version}' == ''    Fail    SeleniumLibrary not installed
    Log    SeleniumLibrary version: ${version}
    Log To Console    SeleniumLibrary: ${version}

