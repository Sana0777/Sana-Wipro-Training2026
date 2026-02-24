*** Settings ***
Resource    ../resources/config.robot
Resource    ../resources/locators.robot
Resource    common_keywords.robot

*** Keywords ***
Search For Product
    [Documentation]    Enter keyword in search box, submit, assert results page.
    [Arguments]    ${keyword}

    Log    STEP 4: SEARCH '${keyword}'

    Input Text    ${LOC_SEARCH_BOX}    ${keyword}
    Element Attribute Value Should Be    ${LOC_SEARCH_BOX}    value    ${keyword}

    Click Element    ${LOC_SEARCH_BTN}

    Sleep    2s
    Log    Search submitted

Assert Search Results Exist
    [Documentation]    Assert at least one result item is visible on the page.
    Wait Until Element Is Visible    ${LOC_RESULT_ITEMS}    timeout=${EXPLICIT_WAIT}
    ...    error=No search results found – result items not visible
    ${count}=    Get Element Count    ${LOC_RESULT_ITEMS}
    Should Be True    ${count} > 0    msg=Search result count is 0
    Log    ${count} result(s) found

Click Product By Name
    [Documentation]    Click on a product title that contains the given name.
    [Arguments]    ${product_name}

    Log    STEP 5: OPEN PRODUCT '${product_name}'

    Wait Until Element Is Visible    ${LOC_PRODUCT_TITLES}    timeout=${EXPLICIT_WAIT}
    ${elements}=    Get WebElements    ${LOC_PRODUCT_TITLES}
    Should Not Be Empty    ${elements}    msg=No product title elements found

    ${clicked}=    Set Variable    ${EMPTY}
    FOR    ${el}    IN    @{elements}
        ${text}=    Get Text    ${el}
        ${text_lower}=    Convert To Lower Case    ${text}
        ${name_lower}=    Convert To Lower Case    ${product_name}
        ${match}=    Run Keyword And Return Status    Should Contain    ${text_lower}    ${name_lower}
        IF    ${match} and '${clicked}' == '${EMPTY}'
            Click Element    ${el}
            Set Test Variable    ${clicked}    ${text}
            Exit For Loop
        END
    END

    IF    '${clicked}' == '${EMPTY}'
        Click Element    ${elements}[0]
        Set Test Variable    ${clicked}    fallback_first
    END

    Log    Clicked product: '${clicked}'
    RETURN    ${clicked}

Assert On Product Detail Page
    [Documentation]    Assert product name visible and return it.
    Wait Until Element Is Visible    ${LOC_PRODUCT_NAME}    timeout=${EXPLICIT_WAIT}
    ...    error=Product name not visible – may not be on product detail page
    ${name}=    Get Text    ${LOC_PRODUCT_NAME}
    Should Not Be Empty    ${name}    msg=Product name text is empty on detail page
    Log    Product detail page: '${name}'
    RETURN    ${name}

Get Product Price
    ${price}=    Get Text    ${LOC_PRODUCT_PRICE}
    Should Not Be Empty    ${price}    msg=Product price is empty
    Log    Price: ${price}
    RETURN    ${price}

Add Product To Cart
    [Documentation]    Set quantity, click Add to Cart, assert success notification.
    [Arguments]    ${quantity}=1

    Log    STEP 6: ADD TO CART (qty=${quantity})

    ${qty_str}=    Convert To String    ${quantity}
    ${has_qty}=    Run Keyword And Return Status
    ...    Element Should Be Visible    ${LOC_QTY_INPUT}
    IF    ${has_qty}
        Clear Element Text    ${LOC_QTY_INPUT}
        Input Text    ${LOC_QTY_INPUT}    ${qty_str}
        Element Attribute Value Should Be    ${LOC_QTY_INPUT}    value    ${qty_str}
    END

    Click Element    ${LOC_ADD_TO_CART_BTN}

    Wait Until Element Is Visible    ${LOC_SUCCESS_NOTIF}    timeout=${EXPLICIT_WAIT}
    ...    error=Success notification not visible after clicking Add to Cart
    ${notif}=    Get Text    ${LOC_SUCCESS_NOTIF}
    Should Not Be Empty    ${notif}    msg=Success notification text is empty
    Should Contain    ${notif}    cart
    ...    msg=Unexpected notification: '${notif}'
    Log    Added to cart. Notification: '${notif}'
    RETURN    ${notif}

Navigate To Cart From Notification
    [Documentation]    Click the 'shopping cart' link in the success notification.
    Wait Until Element Is Visible    ${LOC_CART_NOTIF_LINK}    timeout=${EXPLICIT_WAIT}
    ...    error=Shopping cart link not visible in notification bar
    Click Element    ${LOC_CART_NOTIF_LINK}
    Assert URL Contains    cart
    Log    Navigated to shopping cart