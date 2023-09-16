from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
from allure_commons._allure import step


def test_add_single_row():
    with step('Type text'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Button')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Input')).type('hello@browserstack.com' + '\n')

    with step('Verify added row'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Output')).should(have.text('hello@browserstack.com'))


def test_add_long_string():
    with step('Type text with 100 chars length'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Button')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Input')).type(
            'IyENQukueuGRJbJJKcWYYMTvfbrbSvGgDkVJmyJsmnvRJiRlJylVcflXZefgFlQDzkHFzwaamgFhqFpKlcZFJFfgndKZFKQdbong' + '\n')

    with step('Verify added row is fully visible'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Output')).should(have.text(
            'IyENQukueuGRJbJJKcWYYMTvfbrbSvGgDkVJmyJsmnvRJiRlJylVcflXZefgFlQDzkHFzwaamgFhqFpKlcZFJFfgndKZFKQdbong'))
