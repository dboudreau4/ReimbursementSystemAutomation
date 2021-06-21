Feature: Redirects to different manager pages

  Scenario Outline: Navigate to the View Request Page
    Given The Manager is logged in as <username>
    Given The Manager is on the Manager Portal Page
    When The Manager clicks on the view button for a request
    Then The Manager should be on the View Request Page
    Examples:
      | username |
      | sboudreau |
      | jross     |
      | kross     |
  Scenario Outline: Log out and return to the Manager Login Page
    Given The Manager is logged in as <username>
    Given The Manager is on the Manager Portal Page
    When The Manager clicks on the log out button
    Then The Manager should be on the Manager Login Page
    Examples:
      | username |
      | sboudreau |
      | jross     |
      | kross     |