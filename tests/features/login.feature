Feature: SauceDemo login

    @smoke
    Scenario: Valid user can log in
        Given I am on the SauceDemo login page
        When I log in with username "standard_user" and password "secret_sauce"
        Then I should see the products page

    Scenario: Locked out user sees an error
        Given I am on the SauceDemo login page
        When I log in with username "locked_out_user" and password "secret_sauce"
        Then I should see the error "Sorry, this user has been locked out."