Feature: Employee Login

  Scenario Outline: Employee logs in
    Given The Employee is on the Employee Login Page
    When The Employee types <username> into the username bar
    When The Employee types <password> into the password bar
    When The Employee clicks the login button
    Then The title should be <title>
    Examples:
      | username | password | title |
      | dboudreau | pass    | Employee Portal |
      | joshross  | pass    | Employee Portal |
