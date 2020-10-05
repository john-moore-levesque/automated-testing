from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from local_settings import downloads, additionalChromeOptions
from os import listdir
import time


class Browser():
    def __init__(self):
        self.downloads = downloads()
        self.browser = self.createBrowser()
        self.browser.implicitly_wait(60)

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
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": "%s" %( self.downloads ),
            "download.prompt_for_download": False,
            "download.directory_upgrade": True
        })
        driver = webdriver.Chrome(options=chrome_options)
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
def browser_chrome(context, **kwargs):
    context.browser = Browser()
    yield context.browser
    context.browser.browser.quit()


def before_all(context):
    use_fixture(browser_chrome, context)
