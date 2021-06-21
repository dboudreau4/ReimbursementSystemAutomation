Feature: Manager Approves or Denies a Request

  Scenario Outline: Manger edits a reimbursement
    Given The Manager is logged in as <username>
    Given The Manager has clicked the view request button
    Given The Manager is on the View Request page
    When The Manager selects <status> from the status selector
    When The Manager types <manager_id> into the reviewed by box
    When The Manager types <message> into the message box
    When The Manager clicks the submit button
    When The Manager clicks the return to home page button
    Then The title should be <title>
    Examples:
    | username | status | manager_id | message | title |
    | sboudreau | approved | 1 | Thanks for getting all the supplies we needed | Manager Portal |
    | kross | denied | 1 | We can only approve some of this amount | Manager Portal |
