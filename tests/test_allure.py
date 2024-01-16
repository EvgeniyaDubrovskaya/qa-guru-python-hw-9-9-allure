import allure
from allure_commons.types import Severity
from selene import browser, be
from selene.support import by
from selene.support.shared.jquery_style import s


def test_check_issue_with_allure_step():
    with allure.step("Открываем главную страницу github"):
        browser.open("https://github.com/")

    with allure.step("Ищем страницу репозитория"):
        s(".search-input-container").click()
        s("#query-builder-test").send_keys("eroshenkoam/allure-example")
        s("#query-builder-test").submit()

    with allure.step("Переходим на страницу найденного репозитория"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Переходим на страницу issues"):
        s("#issues-tab").click()
    with allure.step("Проверяем на странице наличие issue 76"):
        s(by.partial_text("#76")).should(be.visible)


def test_check_issue_decorator():
    open_main_page()
    search_repo()
    open_repo_page()
    open_issue_page()
    should_see_issue_number()


@allure.step("Открываем главную страницу github")
def open_main_page():
    browser.open("https://github.com/")


@allure.step("Ищем страницу репозитория")
def search_repo():
    s(".search-input-container").click()
    s("#query-builder-test").send_keys("eroshenkoam/allure-example")
    s("#query-builder-test").submit()


@allure.step("Переходим на страницу найденного репозитория")
def open_repo_page():
    s(by.link_text("eroshenkoam/allure-example")).click()


@allure.step("Переходим на страницу issues")
def open_issue_page():
    s("#issues-tab").click()


@allure.step("Проверяем на странице наличие issue 76")
def should_see_issue_number():
    s(by.partial_text("#76")).should(be.visible)


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "dubrovskaya")
@allure.feature("Issues")
@allure.story("Пользователь видет конкретную issue ")
@allure.link("https://github.com", "Test")
def test_decorator_labels():
    pass


def test_dynamic_labels():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.label("owner", "dubrovskaya")
    allure.dynamic.feature("Issues")
    allure.dynamic.story("Пользователь видет конкретную issue")
    allure.dynamic.link("https://github.com", "Test")
    pass

