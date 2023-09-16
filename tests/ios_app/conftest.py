import allure_commons
import pytest
from appium.options.ios import XCUITestOptions
from selene import browser, support
import project
from appium import webdriver
from utils import allure_helper
import allure


@pytest.fixture(scope='function', autouse=True)
def ios_management():
    options = XCUITestOptions().load_capabilities({
        'app': project.config.app_url,

        'platformName': 'ios',
        'platformVersion': project.config.ios_version,
        'deviceName': project.config.ios_device,

        'bstack:options': {
            'userName': project.config.browserstack_username,
            'accessKey': project.config.browserstack_accesskey,
            'projectName': project.config.project_name,
            'buildName': project.config.build_name,
            'sessionName': project.config.session_name
        }
    })

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(project.config.browserstack_url, options=options)

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    allure_helper.attach_bstack_screenshot()

    allure_helper.attach_bstack_page_source()

    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    allure_helper.attach_bstack_video(session_id)
