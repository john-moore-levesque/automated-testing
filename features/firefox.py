from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from local_settings import downloads, additionalFirefoxOptions
from os import listdir
import time


class Browser():
    def __init__(self):
        self.downloads = downloads()
        self.browser = self.createBrowser()
        self.browser.implicitly_wait(60)

    def createBrowser(self):
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--window-size=1920x1080")
        firefox_options.add_argument("--disable-application-cache")
        firefox_options.add_argument("--verbose")
        firefox_options.add_argument("--disable-notifications")
        additionals = additionalFirefoxOptions()
        if type(additionals) == list:
            for argument in additionals:
                firefox_options.add_argument(argument)
        firefox_options.set_preference("browser.download.dir", "%s" %( self.downloads ))
        firefox_options.set_preference("browser.download.downloadDir", "%s" %( self.downloads ))
        firefox_options.set_preference("browser.download.defaultFolder", "%s" %( self.downloads ))
        firefox_options.set_preference("browser.download.manager.showWhenStarting", False)
        firefox_options.set_preference("browser.helperApps.alwaysAsk.force", False)
        driver = webdriver.Firefox(options=firefox_options)
        return driver

    def clearCache(self):
        self.browser.delete_all_cookies()

    def wait(self, seconds=5):
        time.sleep(seconds)

    def statfile(self, filename, partial=False):
        if not partial:
            try:
                assert filename in listdir(self.downloads)
            except AssertionError:
                print(self.downloads)
                print(listdir(self.downloads))
                return False
        else:
            ispresent = False
            for _ in listdir(self.downloads):
                if filename in _:
                    ispresent = True
            try:
                assert ispresent
            except AssertionError:
                print(self.downloads)
                print(listdir(self.downloads))
                return False

    def listDownloads(self):
        print(self.downloads)
        print(listdir(self.downloads))



@fixture
def browser_firefox(context, **kwargs):
    context.browser = Browser()
    yield context.browser
    context.browser.browser.quit()


def before_all(context):
    use_fixture(browser_firefox, context)
