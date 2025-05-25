*** Settings ***
Documentation   Opens the website: https://www.saucedemo.com/
...             Stores the first item name and price tag to a file
...             Adds the item to the cart
...             Verifies whether correct item has been added to the cart
Library        SeleniumLibrary
#Library        ../library/steps/AddToCart.py
Library        ../library/steps/Login_Logout.py
#Resource        ../library/resources/CDRouter_Precondition.robot

Test Setup    the user logs-in to the website
Test Teardown    the user logs-out from the website

*** Variables ***
${fileName}   itemsDetails.txt
${itemPrice}  0
${cartItem}   Sauce


*** Test Cases ***
Scenario: Stores the given item's name and price tag to a file
    Given the user stores the price of the item '${itemName}' into 'itemPrice'
#    And the user writes the item '${itemName} and price '${itemPrice}' into the file  ${fileName}
#    And the user adds the '${itemName}' to the cart
#    And the user stores the cart item into  ${cartItem}
#    Should Be Equal As Strings    ${cartItem}  ${itemName}

