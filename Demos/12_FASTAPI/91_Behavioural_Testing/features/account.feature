Feature: Account Management

  Scenario: Customer views account details

    Given a registered customer

    When they login with valid credentials

    And they request their account details

    Then the request should succeed

    And the account balance should be returned