*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Test book printed to page
    New Page  ${HOME_URL}
    Fill Text  input[name="author"]  Test-author
    Fill Text  input[name="title"]  Test-title
    Fill Text  input[name="year"]  2026
    Click  input[type="submit"]

    ${book_list}=    Get Text    ul
    Should Contain    ${book_list}    Test-author
    Should Contain    ${book_list}    Test-title
    Should Contain    ${book_list}    2026