Feature: Register Account functionality

  @register
  Scenario: Register with mandatory fields
    Given I navigate to the Register page
    When I enter below details into the mandatory fields
      | first_name | last_name | telephone  | password | confirm_password |
      | Test       | User      | 1234567890 | 12345    | 12345            |
    And I select Privacy Policy option
    And I click on Continue button
    Then Account should get created

  @register
  Scenario: Register with all fields
    Given I navigate to the Register page
    When I enter below details in all fields
      | first_name | last_name | telephone  | password | confirm_password |
      | Test       | User      | 1234567890 | 12345    | 12345            |
    And I select Privacy Policy option
    And I click on Continue button
    Then Account should get created

  @register
  Scenario: Register with a duplicate email address
    Given I navigate to the Register page
    When I enter below details in all fields except email field
      | first_name | last_name | telephone  | password | confirm_password |
      | Test       | User      | 1234567890 | 12345    | 12345            |
    And I enter existing account email into email field
    And I select Privacy Policy option
    And I click on Continue button
    Then Proper warning message about duplicate account should be displayed

  @register
  Scenario: Register without providing any details
    Given I navigate to the Register page
    When I do not enter any details in any fields
    And I click on Continue button
    Then Proper warning message about mandatory fields should be displayed