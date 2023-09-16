import dotenv
import pydantic_settings


class Config(pydantic_settings.BaseSettings):
    browserstack_username: str
    browserstack_accesskey: str
    browserstack_url: str = 'http://hub.browserstack.com/wd/hub'
    app_url: str = 'bs://sample.app'
    project_name: str = 'Mobile Tests Lesson 1'
    build_name: str = 'browserstack-build-1'
    session_name: str = 'BStack first_test'
    android_version: str = '9.0'
    android_device: str = 'Google Pixel 3'
    ios_version: str = '13'
    ios_device: str = 'iPhone 11 Pro'

config = Config(_env_file=dotenv.find_dotenv('.env'))
