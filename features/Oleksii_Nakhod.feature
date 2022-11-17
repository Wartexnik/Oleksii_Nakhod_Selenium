Feature: Work Shift on https://opensource-demo.orangehrmlive.com

  Scenario: Changes are visible on the Work Shifts page
    Given we added a work shift
    When we open the work shifts page
    Then record is added
    When we delete a work shift
    Then record is removed