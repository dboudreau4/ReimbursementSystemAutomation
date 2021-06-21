Feature: Redirects to different employee pages

  Scenario Outline: Navigate to the Request Submission Page
    Given The Employee is logged in as <username>
    Given The Employee is on the Employee Portal Page
    When The Employee clicks on the submit new request button
    Then The Employee should be on the New request form page
    Examples:
      | username |
      | dboudreau |
      | jross |
  Scenario Outline: Log out and return to the Employee Login Page
    Given The Employee is logged in as <username>
    Given The Employee is on the Employee Portal Page
    When The Employee clicks on the log out button
    Then The Employee should be on the Employee Login Page
    Examples:
      | username |
      | dboudreau |
      | jross |