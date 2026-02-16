*** Settings ***
Library           RequestsLibrary
Library           Collections
Suite Setup       Create Session    foodie    http://127.0.0.1:5000
Suite Teardown    Delete All Sessions

*** Variables ***
${USER_EMAIL}         sana01@gmail.com
${USER_PASSWORD}      admin123
${USER_NAME}          Sana
${RESTAURANT_NAME}    Food Fun
${RESTAURANT_CAT}     Veg
${DISH_NAME}          Paneer Butter Masala
${DISH_TYPE}          Main Course

${USER_ID}            None
${RID}                None
${DID}                None
${ORDER_ID}           None
${ORDER_DISHES}       None

*** Keywords ***

Register User
    [Arguments]    ${name}    ${email}    ${password}
    ${payload}=    Create Dictionary    name=${name}    email=${email}    password=${password}
    ${resp}=    POST On Session    foodie    /api/v1/users/register    json=${payload}
    Status Should Be    201    ${resp}
    ${uid}=    Evaluate    int(${resp.json()['id']})
    Set Suite Variable    ${USER_ID}    ${uid}

Register Restaurant
    [Arguments]    ${name}    ${category}    ${location}    ${images}    ${contact}
    ${payload}=    Create Dictionary    name=${name}    category=${category}    location=${location}    images=${images}    contact=${contact}
    ${resp}=    POST On Session    foodie    /api/v1/restaurants    json=${payload}
    Status Should Be    201    ${resp}
    ${rid}=    Evaluate    int(${resp.json()['id']})
    Set Suite Variable    ${RID}    ${rid}

Approve Restaurant
    ${resp}=    PUT On Session    foodie    /api/v1/admin/restaurants/${RID}/approve
    Status Should Be    200    ${resp}
    Should Be Equal    ${resp.json()['message']}    Restaurant approved

Add Dish
    [Arguments]    ${restaurant_id}    ${name}    ${type}    ${price}    ${available_time}    ${image}
    ${payload}=    Create Dictionary    name=${name}    type=${type}    price=${price}    available_time=${available_time}    image=${image}
    ${resp}=    POST On Session    foodie    /api/v1/restaurants/${restaurant_id}/dishes    json=${payload}
    Status Should Be    201    ${resp}
    ${did}=    Evaluate    int(${resp.json()['id']})
    Set Suite Variable    ${DID}    ${did}
    ${dish_list}=    Create List    ${did}
    Set Suite Variable    ${ORDER_DISHES}    ${dish_list}

Place Order
    ${uid}=    Evaluate    int(${USER_ID})
    ${rid}=    Evaluate    int(${RID})
    ${dish_list}=    Create List
    ${dish_int}=    Evaluate    int(${DID})
    Append To List    ${dish_list}    ${dish_int}

    ${payload}=    Create Dictionary
    ...    user_id=${uid}
    ...    restaurant_id=${rid}
    ...    dishes=${dish_list}

    ${resp}=    POST On Session    foodie    /api/v1/orders    json=${payload}
    Status Should Be    201    ${resp}

    ${oid}=    Evaluate    int(${resp.json()['id']})
    Set Suite Variable    ${ORDER_ID}    ${oid}

Give Rating
    ${oid}=    Evaluate    int(${ORDER_ID})
    ${payload}=    Create Dictionary    order_id=${oid}    rating=5    comment=Excellent
    ${resp}=    POST On Session    foodie    /api/v1/ratings    json=${payload}
    Status Should Be    201    ${resp}
    Should Be Equal As Integers    ${resp.json()['rating']}    5

*** Test Cases ***

User Registration - Success
    Register User    ${USER_NAME}    ${USER_EMAIL}    ${USER_PASSWORD}

User Registration - Duplicate
    ${payload}=    Create Dictionary    name=${USER_NAME}    email=${USER_EMAIL}    password=${USER_PASSWORD}
    ${resp}=    POST On Session    foodie    /api/v1/users/register    json=${payload}    expected_status=409
    Status Should Be    409    ${resp}

Register Restaurant
    Register Restaurant    ${RESTAURANT_NAME}    ${RESTAURANT_CAT}    Delhi    img.jpg    123456

View Restaurant Profile
    ${resp}=    GET On Session    foodie    /api/v1/restaurants/${RID}
    Status Should Be    200    ${resp}
    Should Be Equal As Integers    ${resp.json()['id']}    ${RID}

Update Restaurant
    ${payload}=    Create Dictionary    location=Mumbai
    ${resp}=    PUT On Session    foodie    /api/v1/restaurants/${RID}    json=${payload}
    Status Should Be    200    ${resp}
    Should Be Equal    ${resp.json()['location']}    Mumbai

Search Restaurants
    ${params}=    Create Dictionary    name=Food
    ${resp}=    GET On Session    foodie    /api/v1/restaurants/search    params=${params}
    Status Should Be    200    ${resp}


Add Dish
    Add Dish    ${RID}    ${DISH_NAME}    ${DISH_TYPE}    250    Lunch    paneer.jpg

Approve Restaurant
    Approve Restaurant

Place Order
    Place Order

View Orders By User
    ${resp}=    GET On Session    foodie    /api/v1/users/${USER_ID}/orders
    Status Should Be    200    ${resp}
    Should Be Equal As Integers    ${resp.json()[0]['id']}    ${ORDER_ID}

View Orders By Restaurant
    ${resp}=    GET On Session    foodie    /api/v1/restaurants/${RID}/orders
    Status Should Be    200    ${resp}
    Should Be Equal As Integers    ${resp.json()[0]['id']}    ${ORDER_ID}

Give Rating
    Give Rating


Disable Restaurant (Admin)
    ${resp}=    PUT On Session    foodie    /api/v1/admin/restaurants/${RID}/disable
    Status Should Be    200    ${resp}
    Should Be Equal    ${resp.json()['message']}    Restaurant disabled

View Admin Orders
    ${resp}=    GET On Session    foodie    /api/v1/admin/orders
    Status Should Be    200    ${resp}

View Admin Feedback
    ${resp}=    GET On Session    foodie    /api/v1/admin/feedback
    Status Should Be    200    ${resp}
