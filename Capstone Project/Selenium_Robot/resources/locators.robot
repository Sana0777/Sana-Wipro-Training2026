*** Variables ***

${LOC_REG_LINK}             xpath=//a[text()='Register']
${LOC_GENDER_MALE}          id=gender-male
${LOC_GENDER_FEMALE}        id=gender-female
${LOC_FIRST_NAME}           id=FirstName
${LOC_LAST_NAME}            id=LastName
${LOC_REG_EMAIL}            id=Email
${LOC_REG_PASSWORD}         id=Password
${LOC_CONFIRM_PASSWORD}     id=ConfirmPassword
${LOC_REGISTER_BTN}         id=register-button
${LOC_REGISTER_RESULT}      css=div.result


${LOC_LOGIN_LINK}           xpath=//a[text()='Log in']
${LOC_LOGIN_EMAIL}          id=Email
${LOC_LOGIN_PASSWORD}       id=Password
${LOC_LOGIN_BTN}            xpath=//input[@value='Log in']
${LOC_LOGIN_ERROR}          css=div.validation-summary-errors span
${LOC_ACCOUNT_LINK}         css=a.account
${LOC_LOGOUT_LINK}          xpath=//a[text()='Log out']


${LOC_SEARCH_BOX}           id=small-searchterms
${LOC_SEARCH_BTN}           xpath=//input[@value='Search']
${LOC_RESULT_ITEMS}         css=div.product-item
${LOC_PRODUCT_TITLES}       css=h2.product-title a


${LOC_PRODUCT_NAME}         css=div.product-name h1
${LOC_PRODUCT_PRICE}        css=div.product-price span
${LOC_QTY_INPUT}            css=input.qty-input
${LOC_ADD_TO_CART_BTN}      xpath=//input[@value='Add to cart']
${LOC_SUCCESS_NOTIF}        css=div.bar-notification.success p.content
${LOC_CART_NOTIF_LINK}      xpath=//a[text()='shopping cart']


${LOC_CART_ROWS}            css=tr.cart-item-row
${LOC_CART_PRODUCT_NAMES}   css=td.product a
${LOC_CART_QTY_INPUTS}      css=input.qty-input
${LOC_CART_REMOVE_CHECKS}   css=input[name='removefromcart']
${LOC_UPDATE_CART_BTN}      xpath=//input[@name='updatecart']
${LOC_CART_EMPTY_MSG}       xpath=//div[contains(@class,'order-summary-content')]//p[contains(text(),'cart is empty') or contains(text(),'shopping cart is empty')]