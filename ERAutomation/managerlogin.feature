Feature: Manager Login

  Scenario Outline: Manager logs in
    Given The Manager is on the Manager Login Page
    When The Manager types <username> into the username bar
    When The Manager types <password> into the password bar
    When The Manager clicks the login button
    Then The page title should be <title>
    Examples:
      | username | password | title |
      | sboudreau | pass    | Manager Portal |
      | jross  | pass    | Manager Portal |