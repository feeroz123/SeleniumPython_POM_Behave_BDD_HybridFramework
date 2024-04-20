Feature: Search Functionality

  @search
  Scenario: Search for a valid product
    Given Navigate to the Home page
    When I enter a valid product as "HP" in the Search box
    And I click on Search button
    Then Valid product should get displayed in the search results

  @search
  Scenario: Search for an invalid product
    Given Navigate to the Home page
    When I enter an invalid product as "Honda" in the Search box
    And I click on Search button
    Then Proper message should be displayed in the search results

  @search
  Scenario: Search without entering any product
    Given Navigate to the Home page
    When I do not enter anything in the Search box
    And I click on Search button
    Then Proper message should be displayed in the search results
