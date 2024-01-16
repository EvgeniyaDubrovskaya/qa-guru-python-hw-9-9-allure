from selene import browser, be, by
from selene.support.shared.jquery_style import s


def test_check_issue():
    browser.open("https://github.com/")
    s(".search-input-container").click()
    s("#query-builder-test").send_keys("eroshenkoam/allure-example")
    s("#query-builder-test").submit()

    s(by.link_text("eroshenkoam/allure-example")).click()
    s("#issues-tab").click()

    s(by.partial_text("#76")).should(be.visible)

