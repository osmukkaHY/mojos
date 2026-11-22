*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Test new book printed to page
    New Page  ${HOME_URL}/inproceedings
    Fill Text  input[name="reference_name"]  Test-Refname
    Fill Text  input[name="author"]  Test-Author
    Fill Text  input[name="title"]  Test-Title
    Fill Text  input[name="year"]  2026
    Fill Text  input[name="series"]  Test-Series
    Fill Text  input[name="pages"]  45-54
    Click  input[type="submit"]
    Get Text  text=Kirjoittaja: Test-Author
    Get Text  text=Nimi: Test-Title
    Get Text  text=Julkaisuvuosi: 2026

