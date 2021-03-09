from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from local_settings import additionalChromeOptions, scratchDir
from os import listdir
import time


class Browser():
    def __init__(self):
        self.browser = self.createBrowser()
        self.browser.implicitly_wait(60)
        self.scratch = scratchDir()

    def createBrowser(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument("--disable-application-cache")
        chrome_options.add_argument("--verbose")
        chrome_options.add_argument("--disable_notifications")
        additionals = additionalChromeOptions()
        if type(additionals) == list:
            for argument in additionals:
                chrome_options.add_argument(argument)
        driver = webdriver.Chrome(options=chrome_options)
        return driver

    def clearCache(self):
        self.browser.delete_all_cookies()

    def wait(self, seconds=5):
        time.sleep(seconds)

    def disappeared(self, xpath):
        checkThingDisappeared(self.browser, xpath)


@fixture
def browser_chrome(context, **kwargs):
    context.browser = Browser()
    yield context.browser
    context.browser.browser.quit()


def before_all(context):
    use_fixture(browser_chrome, context)
