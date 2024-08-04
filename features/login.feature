Feature: Login functionality

  @login
  Scenario: Login with valid credentials
    Given I am in login page
    When I enter valid email address and password into the fields
    And I click on login button
    Then I should get logged in

  @login
  Scenario: Login with invalid email and valid password
    Given I am in login page
    When I enter invalid email address and valid password into the fields
    And I click on login button
    Then I should get an error message

  @login
  Scenario: Login with valid email and invalid password
    Given I am in login page
    When I enter valid email address and invalid password into the fields
    And I click on login button
    Then I should get an error message

  @login
  Scenario: Login with invalid credentials
    Given I am in login page
    When I enter invalid email address and invalid password into the fields
    And I click on login button
    Then I should get an error message

  @login
  Scenario: Login without entering any credentials
    Given I am in login page
    When I do not enter anything in email address and password fields
    And I click on login button
    Then I should get an error message



