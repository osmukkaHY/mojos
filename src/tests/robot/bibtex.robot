*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Test Print Bibtex Button Exists
    New Page  ${HOME_URL}/book
    Fill Text  input[name="reference_name"]  Bibtex-Button-Ref
    Fill Text  input[name="author"]  Bibtex-Button-Author
    Fill Text  input[name="title"]  Bibtex-Button-Title
    Fill Text  input[name="year"]  2026
    Fill Text  input[name="publisher"]  Bibtex-Button-Publisher
    Fill Text  input[name="tag"]  Bibtex-Button-Tag
    Click  input[type="submit"]
    New Page  ${HOME_URL}
    ${button_count}=  Get Element Count  text=Tulosta BibTeX
    Should Be True  ${button_count} > 0

Test Pressing Generate Bibtex Prints Bibtex Format With Correct Data
    New Page  ${HOME_URL}/book
    Fill Text  input[name="reference_name"]  Bibtex-Data-Ref
    Fill Text  input[name="author"]  Bibtex-Data-Author
    Fill Text  input[name="title"]  Bibtex-Data-Title
    Fill Text  input[name="year"]  2025
    Fill Text  input[name="publisher"]  Bibtex-Data-Publisher
    Fill Text  input[name="tag"]  Bibtex-Data-Tag
    Click  input[type="submit"]
    New Page  ${HOME_URL}
    Click  xpath=//li[contains(., 'Bibtex-Data-Ref')]//button[.="Tulosta BibTeX"]
    ${bibtex}=  Get Text  css=pre
    Should Contain  ${bibtex}  @book{Bibtex-Data-Ref,
    Should Contain  ${bibtex}  author = {Bibtex-Data-Author}
    Should Contain  ${bibtex}  title = {Bibtex-Data-Title}
    Should Contain  ${bibtex}  year = {2025}
    Should Contain  ${bibtex}  publisher = {Bibtex-Data-Publisher}
