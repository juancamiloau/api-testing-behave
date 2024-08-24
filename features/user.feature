Feature: Pet store user API

  Scenario: Create user
    When I create the user
    Then I should see 200 status code
    And I should see the data when I get the user

  Scenario: Modify user
    Given I have created a new user
    When I modify the user
    Then I should see the data when I get the user

  Scenario: Delete user
    Given I have created a new user
    When I delete the user
    Then I should see 200 status code
    Then I should get user not found when I get it