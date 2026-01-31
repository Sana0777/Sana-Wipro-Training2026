*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${URL}            https://www.google.com
${BROWSER}        chrome

*** Test Cases ***
Open And Verify Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Title Should Be    Google
    Capture Page Screenshot
    Close Browser
