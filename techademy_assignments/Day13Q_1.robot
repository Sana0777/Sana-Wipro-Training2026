*** Settings ***
Library    SeleniumLibrary
Library        SeleniumLibrary
*** Test Cases ***
Open And Verify Page
    Open Browser    https://google.com    chrome
    Title Should Be    google
    Capture Page Screenshot    screenshot.png
    Close Browser
