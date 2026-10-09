from pytest_bdd import scenarios, given, when, then, parsers

scenarios("features/login.feature")


@given("I am on the SauceDemo login page")
def open_login(page):
    page.goto("https://www.saucedemo.com")


@when(parsers.parse('I log in with username "{user}" and password "{pwd}"'))
def login(page, user, pwd):
    page.fill("#user-name", user)
    page.fill("#password", pwd)
    page.click("#login-button")


@then("I should see the products page")
def products_page(page):
    assert page.url.endswith("/inventory.html")
    assert page.locator(".title").inner_text() == "Products"


@then(parsers.parse('I should see the error "{message}"'))
def error_shown(page, message):
    assert message in page.locator('[data-test="error"]').inner_text()