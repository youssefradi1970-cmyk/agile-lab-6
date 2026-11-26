# Part D: Gherkin scenarios for our project story

**Story:** As a student, I want to request a transcript so that I can submit it to an employer.

```gherkin
Feature: Transcript request

  Scenario: Happy path - request a transcript
    Given a student with ID "2023001" who has no unpaid fees
    When the student requests a transcript
    Then the request is accepted
    And the student sees the status "Pending"

  Scenario: Refused - the student has unpaid fees
    Given a student with ID "2023001" who has unpaid fees
    When the student requests a transcript
    Then the request is refused with "unpaid fees"
    And no request is created

  Scenario Outline: Edge - number of copies
    Given a student with ID "2023001" who has no unpaid fees
    When the student requests <copies> copies of the transcript
    Then the result is "<result>"

    Examples:
      | copies | result   |
      | 1      | accepted |
      | 5      | accepted |
      | 6      | refused  |
      | 0      | refused  |
```