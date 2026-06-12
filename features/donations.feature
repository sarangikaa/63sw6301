Feature: Donation Management for Non-Profit Animal Charity

  As a donor
  I want to make donations to the charity
  So that I can support animal welfare activities

  Scenario: Successful donation submission
    Given the donation system is running
    When I donate 50 pounds
    Then the donation should be recorded successfully
    And the total donations should be 50

  Scenario: Multiple donations accumulation
    Given the donation system is running
    When I donate 30 pounds
    And I donate 20 pounds
    Then the total donations should be 50

  Scenario: Invalid donation amount
    Given the donation system is running
    When I donate -10 pounds
    Then the system should reject the donation
    And the error message should be "Invalid donation amount"
