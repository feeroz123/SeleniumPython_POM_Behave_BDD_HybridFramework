Feature: Login functionality

  @login
  Scenario: Login with valid credentials
    Given I am on the login page
    When I enter valid email address and valid password into the fields
    And I click on the login button
    Then I should get logged in

  @login
  Scenario: Login with invalid email and valid password
    Given I am on the login page
    When I enter invalid email address and valid password into the fields
    And I click on the login button
    Then I should get a proper warning message

  @login
  Scenario: Login with valid email and invalid password
    Given I am on the login page
    When I enter valid email address and invalid password into the fields
    And I click on the login button
    Then I should get a proper warning message

  @login
  Scenario: Login with invalid email and invalid password
    Given I am on the login page
    When I enter invalid email address and invalid password into the fields
    And I click on the login button
    Then I should get a proper warning message

  @login
  Scenario: Login without entering any credentials
    Given I am on the login page
    When I do not enter any credentials
    And I click on the login button
    Then I should get a proper warning message
