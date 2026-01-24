Feature: Money transfer

Scenario: User is able to successfully transfer funds between two accounts
    Given Account registry is empty
    And I create an account using name: "alice", last name: "smith", pesel: "12345678901" with balance: "1000"
    And I create an account using name: "bob", last name: "johnson", pesel: "10987654321" with balance: "500"
    When I transfer out "200" from account with pesel: "12345678901"
    When I transfer in "200" to account with pesel: "10987654321"
    Then Account with pesel "12345678901" has balance equal to "800"
    And Account with pesel "10987654321" has balance equal to "700"

Scenario: User attempts to transfer more funds than available in their account
    Given Account registry is empty
    And I create an account using name: "charlie", last name: "brown", pesel: "22334455667" with balance: "300"
    When I fail to transfer out "500" from account with pesel: "22334455667"
    And Account with pesel "22334455667" has balance equal to "300"

Scenario: User is able to transfer funds to their own account
    Given Account registry is empty
    And I create an account using name: "eve", last name: "adams", pesel: "33445566778" with balance: "250"
    When I transfer in "50" to account with pesel: "33445566778"
    Then Account with pesel "33445566778" has balance equal to "300"

