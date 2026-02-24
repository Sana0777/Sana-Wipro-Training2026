*** Settings ***
Resource    ../resources/config.robot
Resource    ../resources/locators.robot
Resource    common_keywords.robot

*** Keywords ***
Clear Cart
    Go To    ${BASE_URL}/cart
    Sleep    1s
    ${count}=    Get Element Count    ${LOC_CART_ROWS}
    IF    ${count} == 0
        Log    Cart already empty — skipping clear    INFO
        RETURN
    END
    Log    Clearing ${count} leftover item(s)    WARN
    ${checkboxes}=    Get WebElements    ${LOC_CART_REMOVE_CHECKS}
    FOR    ${cb}    IN    @{checkboxes}
        Click Element    ${cb}
    END
    Click Element    ${LOC_UPDATE_CART_BTN}
    Sleep    2s
    ${empty_msg_shown}=    Run Keyword And Return Status
    ...    Element Should Be Visible    ${LOC_CART_EMPTY_MSG}
    ${rows_left}=    Get Element Count    ${LOC_CART_ROWS}
    ${is_empty}=    Evaluate    ${empty_msg_shown} or ${rows_left} == 0
    Should Be True    ${is_empty}    msg=Cart did not empty after clicking update
    Log    Cart cleared successfully    INFO

Assert Cart Not Empty
    Wait Until Element Is Visible    ${LOC_CART_ROWS}    timeout=${EXPLICIT_WAIT}
    ...    error=Cart appears empty - no cart item rows found
    ${count}=    Get Element Count    ${LOC_CART_ROWS}
    Should Be True    ${count} > 0    msg=Cart row count is 0
    Log    Cart has ${count} item(s)    INFO
    RETURN    ${count}

Assert Product In Cart
    [Arguments]    ${product_name}
    Wait Until Element Is Visible    ${LOC_CART_PRODUCT_NAMES}    timeout=${EXPLICIT_WAIT}
    ${elements}=    Get WebElements    ${LOC_CART_PRODUCT_NAMES}
    ${found}=    Set Variable    ${FALSE}
    FOR    ${el}    IN    @{elements}
        ${text}=      Get Text              ${el}
        ${t_lower}=   Convert To Lower Case    ${text}
        ${n_lower}=   Convert To Lower Case    ${product_name}
        ${match}=     Run Keyword And Return Status    Should Contain    ${t_lower}    ${n_lower}
        IF    ${match}
            Set Test Variable    ${found}    ${TRUE}
        END
    END
    Should Be True    ${found}
    ...    msg=Product '${product_name}' not found in cart
    Log    Product '${product_name}' confirmed in cart    INFO

Get Cart Item Quantity
    [Arguments]    ${index}=0
    ${inputs}=    Get WebElements    ${LOC_CART_QTY_INPUTS}
    ${qty}=       Get Element Attribute    ${inputs}[${index}]    value
    Log    Qty at index ${index}: ${qty}    INFO
    RETURN    ${qty}

Assert Cart Quantity Equals
    [Arguments]    ${expected}    ${index}=0
    ${qty_str}=    Convert To String    ${expected}
    ${actual}=     Get Cart Item Quantity    ${index}
    Should Be Equal    ${actual}    ${qty_str}
    ...    msg=Cart qty mismatch: expected '${qty_str}', got '${actual}'
    Log    Cart qty confirmed: ${actual}    INFO

Update Cart Quantity
    [Arguments]    ${new_quantity}    ${index}=0
    Log    STEP 8: UPDATE QTY to ${new_quantity}    INFO
    ${count}=    Get Element Count    ${LOC_CART_ROWS}
    Should Be True    ${count} > 0    msg=Cart is empty
    ${qty_str}=    Convert To String    ${new_quantity}
    ${inputs}=     Get WebElements    ${LOC_CART_QTY_INPUTS}
    Clear Element Text    ${inputs}[${index}]
    Input Text            ${inputs}[${index}]    ${qty_str}
    Element Attribute Value Should Be    ${inputs}[${index}]    value    ${qty_str}
    Click Element    ${LOC_UPDATE_CART_BTN}
    Wait Until Element Is Visible    ${LOC_CART_QTY_INPUTS}    timeout=10
    Assert Cart Quantity Equals    ${new_quantity}    ${index}
    Log    Quantity updated and verified: ${new_quantity}    INFO

Remove Item From Cart
    [Arguments]    ${index}=0
    Log    STEP 9: REMOVE ITEM    INFO
    ${count_before}=    Get Element Count    ${LOC_CART_ROWS}
    Should Be True    ${count_before} > 0    msg=Cart is empty
    ${checkboxes}=    Get WebElements    ${LOC_CART_REMOVE_CHECKS}
    Click Element    ${checkboxes}[${index}]
    Log    Remove checkbox checked at index ${index}    INFO
    Click Element    ${LOC_UPDATE_CART_BTN}
    Sleep    2s
    # Check empty message OR zero rows — either confirms cart is empty
    ${empty_msg_shown}=    Run Keyword And Return Status
    ...    Element Should Be Visible    ${LOC_CART_EMPTY_MSG}
    ${rows_remaining}=    Get Element Count    ${LOC_CART_ROWS}
    ${is_empty}=    Evaluate    ${empty_msg_shown} or ${rows_remaining} == 0
    Should Be True    ${is_empty}
    ...    msg=Cart did not empty after removing item
    Log    Item removed. Cart: ${count_before} to ${rows_remaining}    INFO
    Log    Cart is now empty    INFO
    RETURN    ${rows_remaining}

Assert Cart Is Empty
    ${count}=    Get Element Count    ${LOC_CART_ROWS}
    Should Be Equal As Integers    ${count}    0
    ...    msg=Cart is not empty - ${count} item(s) still present
    Log    Cart empty confirmed    INFO