Feature:  Register functionality

  Background: Common steps
    Given I am in register page

  @register
  Scenario: Register with mandatory fields
    When I enter mandatory fields
    And I select privacy policy option
    And I click on Continue button
    Then Account should get created

  @register
  Scenario: Register will all fields
    When I enter all fields
    And I select privacy policy option
    And I click on Continue button
    Then Account should get created

  @register
  Scenario: Register with duplicate email address
    When I enter details into all fields except email field
    And I enter existing email address into email field
    And I select privacy policy option
    And I click on Continue button
    Then A proper error message should be shown

  @register
  Scenario: Register without providing any details
    When I do not enter anything in the fields
    And I click on Continue button
    Then A proper error message should be shown for mandatory fields



