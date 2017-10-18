*** Settings ***
Documentation    Suite description
Library  ScriptLibrary.Demo
Library  Selenium2Library

*** Test Cases ***
Test title
    [Tags]    DEBUG
    [Setup]  Provided precondition
    When Log    action
        do something
    Then Log    check expectations
    [Teardown]  close all browsers

*** Keywords ***
Provided precondition
    Log  Setup system under test
    open browser  url=https://www.baidu.com/    browser=chrome