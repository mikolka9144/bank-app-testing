Feature: Account registry

Scenario: User is able to create 2 accounts
    Given Account registry is empty
    When I create an account using name: "kurt", last name: "cobain", pesel: "89092909246"
    And I create an account using name: "tadeusz", last name: "szcześniak", pesel: "79101011234"
    Then Number of accounts in registry equals: "2"
    And Account with pesel "89092909246" exists in registry
    And Account with pesel "79101011234" exists in registry

Scenario: User is able to update surname of already created account
    Given Account registry is empty
    And I create an account using name: "nata", last name: "haydamaky", pesel: "95092909876"
    When I update "last_name" of account with pesel: "95092909876" to "filatov"
    Then Account with pesel "95092909876" has "last_name" equal to "filatov"

Scenario: User is able to update name of already created account
    Given Account registry is empty
    And I create an account using name: "michael", last name: "jackson", pesel: "02020202020"
    When I update "first_name" of account with pesel: "02020202020" to "prince"
    Then Account with pesel "02020202020" has "first_name" equal to "prince"

Scenario: Created account has all fields correctly set
    Given Account registry is empty
    When I create an account using name: "john", last name: "doe", pesel: "03030303030"
    Then Account with pesel "03030303030" has "first_name" equal to "john"
    And Account with pesel "03030303030" has "last_name" equal to "doe"

Scenario: User is able to delete created account
    Given Account registry is empty
    And I create an account using name: "parov", last name: "stelar", pesel: "01092909876"
    When I delete account with pesel: "01092909876"
    Then Account with pesel "01092909876" does not exist in registry
    And Number of accounts in registry equals: "0"
