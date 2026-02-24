*** Settings ***
Documentation
...    End To End Full Flow Suite – demowebshop.tricentis.com

Library     SeleniumLibrary    screenshot_root_directory=${CURDIR}/../reports
Library     Collections
Library     String
Library     OperatingSystem

Resource    ../resources/config.robot
Resource    ../resources/locators.robot
Resource    ../keywords/common_keywords.robot
Resource    ../keywords/register_keywords.robot
Resource    ../keywords/login_keywords.robot
Resource    ../keywords/product_keywords.robot
Resource    ../keywords/cart_keywords.robot

Suite Teardown    Close All Browsers
Test Teardown     Run Keyword And Ignore Error    Close Browser Session

*** Test Cases ***
Complete Journey of - User 1
    Run E2E For Row    0

Complete Journey of - User 2
    Run E2E For Row    1

Complete Journey of - User 3
    Run E2E For Row    2

Complete Journey of - User 4
    Run E2E For Row    3

Complete Journey of - User 5
    Run E2E For Row    4

*** Keywords ***
Run E2E For Row
    [Arguments]    ${row_index}
    ${content}=          Get File          ${CURDIR}/../variables/test_data.csv
    ${lines}=            Split To Lines    ${content}
    ${line_num}=         Evaluate          ${row_index} + 1
    ${line}=             Strip String      ${lines}[${line_num}]
    ${cols}=             Split String      ${line}    ,
    ${first_name}=       Strip String      ${cols}[0]
    ${last_name}=        Strip String      ${cols}[1]
    ${email}=            Strip String      ${cols}[2]
    ${password}=         Strip String      ${cols}[3]
    ${gender}=           Strip String      ${cols}[4]
    ${product_search}=   Strip String      ${cols}[5]
    ${product_name}=     Strip String      ${cols}[6]
    ${add_quantity}=     Strip String      ${cols}[7]
    ${updated_quantity}=    Strip String   ${cols}[8]
    Run E2E For Single User
    ...    ${first_name}    ${last_name}    ${email}    ${password}    ${gender}
    ...    ${product_search}    ${product_name}    ${add_quantity}    ${updated_quantity}

Run E2E For Single User
    [Arguments]
    ...    ${first_name}    ${last_name}    ${email}    ${password}    ${gender}
    ...    ${product_search}    ${product_name}    ${add_quantity}    ${updated_quantity}

    # STEP 1: Open browser and verify site loaded
    Open Browser To Site
    ${title}=    Get Title
    Should Not Be Empty    ${title}    msg=Page title empty - site not loaded

    # STEP 2: Register
    ${reg_result}=    Register New User
    ...    ${first_name}    ${last_name}    ${email}    ${password}    ${gender}
    Should Not Be Empty    ${reg_result}
    Log    Registration result: ${reg_result}

    # STEP 3: Login — always perform full visible login
    Go To    ${BASE_URL}
    ${already_logged_in}=    Run Keyword And Return Status
    ...    Element Should Be Visible    ${LOC_ACCOUNT_LINK}
    IF    ${already_logged_in}
        Log    Auto-session detected — logging out to show fresh login
        Logout User
        Go To    ${BASE_URL}
        Wait Until Element Is Visible    ${LOC_LOGIN_LINK}    timeout=8
    END
    Login As User    ${email}    ${password}

    # Clear cart silently — safety net for failed previous runs
    Clear Cart

    # STEP 4: Search for product
    Go To    ${BASE_URL}
    Wait Until Element Is Visible    ${LOC_SEARCH_BOX}    timeout=8
    Search For Product    ${product_search}
    Assert Search Results Exist

    # STEP 5: Open product detail
    Click Product By Name    ${product_name}
    ${actual_product_name}=    Assert On Product Detail Page
    Get Product Price

    # STEP 6: Add to cart
    ${add_qty}=    Convert To Integer    ${add_quantity}
    Add Product To Cart    ${add_qty}

    # STEP 7: Navigate to cart and verify
    Navigate To Cart From Notification
    Assert Cart Not Empty
    Assert Product In Cart    ${actual_product_name}
    Assert Cart Quantity Equals    ${add_qty}    0

    # STEP 8: Update quantity
    ${upd_qty}=    Convert To Integer    ${updated_quantity}
    Update Cart Quantity    ${upd_qty}    0

    # STEP 9: Remove item from cart
    ${remaining}=    Remove Item From Cart    0
    Should Be Equal As Integers    ${remaining}    0
    ...    msg=Expected 0 items after removal, got ${remaining}

    # STEP 10: Logout
    Logout User