Feature: Employee Submits Request

  Scenario Outline: Employee submits a reimbursement
    Given The Employee is logged in as <username>
    Given The Employee has clicked the submit new request button
    Given The Employee is on the New request form page
    When The Employee types <amount> into the amount bar
    When The Employee types <reason> into the reason bar
    When The Employee clicks the submit button
    When The Employee clicks the return to home page button
    Then The title should be <title>
    Examples:
    | username | amount | reason | title |
    | dboudreau  | 1000 | Business trip expenses | Employee Portal |
