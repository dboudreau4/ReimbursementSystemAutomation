Feature: Redirects Manager back to home or login pages

  Scenario Outline: Go from Statistics to the Manager Portal Page
    Given The Manager is logged in as <username>
    Given The Manager has clicked on the View Statistics Button
    Given The Manager is on the Statistics Page
    When The Manager clicks on Return to Manager Portal Button
    Then The title should be <title>
    Examples:
      | username | title |
      | sboudreau | Manager Portal |
      | jross | Manager Portal |
      | bdurgiah | Manager Portal |


  Scenario Outline: Log out from Statistics Page
  Given The Manager is logged in as <username>
  Given The Manager has clicked on the View Statistics Button
  Given The Manager is on the Statistics Page
  When The Manager clicks on the stats log out button
  Then The title should be <title>
  Examples:
    | username | title |
    | sboudreau | Manager Login |
    | jross | Manager Login |
    | bdurgiah | Manager Login |