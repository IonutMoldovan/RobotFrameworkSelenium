*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://www.wikipedia.org
${BROWSER}    Chrome

*** Test Cases ***
Test Open Wikipedia
    [Documentation]    This test case will open https://www.wikipedia.org, check the title, and close the browser.
    Open Browser    ${URL}    ${BROWSER}
    SeleniumLibrary.Capture Page Screenshot
    Title Should Be    Wikipedia
    SeleniumLibrary.Capture Page Screenshot
    Close Browser
