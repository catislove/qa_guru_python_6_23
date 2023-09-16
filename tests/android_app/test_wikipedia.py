from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def test_search_article_by_title():
    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Appium')

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


def test_open_article_on_main_page():
    with step('Tap on article in News section'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/horizontal_scroll_list_item_text')).click()

    with step('Verify page is opened with some content'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/horizontal_scroll_list_item_text')).should(
            be.not_.present)
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/view_news_fullscreen_story_text')).should(be.present)
