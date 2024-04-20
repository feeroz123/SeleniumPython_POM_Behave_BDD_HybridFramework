Feature: Login functionality

  @login
  Scenario Outline: Login with valid credentials
    Given I am on the login page
    When I enter valid email address as "<email>" and valid password as "<password>" into the fields
    And I click on the login button
    Then I should get logged in
    Examples:
      | email                       | password      |
      | automation_user@yopmail.com | Automation123 |

  @login
  Scenario Outline: Login with different email and password combinations for failure analysis
    Given I am on the login page
    When I enter an email as "<email>" and a password as "<password>" into the fields
    And I click on the login button
    Then I should get a proper warning message
    Examples:
      | email                       | password        |
      | invalid_user@yopmail.com    | Automation123   |
      | automation_user@yopmail.com | InvalidPassword |
      | invalid_user@yopmail.com    | InvalidPassword |

  @login
  Scenario: Login without entering any credentials
    Given I am on the login page
    When I do not enter any credentials
    And I click on the login button
    Then I should get a proper warning message

