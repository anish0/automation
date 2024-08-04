Feature: Search functionality

  @search
  Scenario: Search for a valid product
    Given I am in homepage
    When I enter valid product in the search box
    And I click on search button
    Then Valid product should get displayed in search result

  @search
  Scenario: Search for an invalid product
    Given I am in homepage
    When I enter invalid product in the search box
    And I click on search button
    Then Proper error message should be displayed

  @search
  Scenario: Search without entering the product
    Given I am in homepage
    When I do not enter anything in the search box
    And I click on search button
    Then Proper error message should be displayed