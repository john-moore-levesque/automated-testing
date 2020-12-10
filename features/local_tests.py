from os import environ, stat
from dotenv import load_dotenv
from local_settings import authInformation, checkFirefox, checkChrome
from chrome import Browser as Chrome
from firefox import Browser as Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from behave import *
from local_authentication import *

'''
This file contains versions of the test scripts that can be easily run from the
command line. If you need to do lots of debugging and testing, it can be helpful
to just run the individual commands of a test file, rather than doing a full
test. For instance, if you have a test that's not finding a button you expect
it to find, you can use the functions in this file to help figure out exactly
what behave is seeing when you run it.
'''
def env(envfile=".env"):
    try:
        stat(envfile)
    except FileNotFoundError:
        return False
    load_dotenv(envfile)

def createBrowser():
    chrome = checkChrome()
    firefox = checkFirefox()
    if chrome:
        return Chrome()
    elif firefox:
        return Firefox()
    else:
        return False

def getElement(browser, elementType, identifier, property=False):
    elements = browser.browser.find_elements_by_tag_name("%s" %(elementType))
    best = set()
    attributeList = ["title", "value", "placeholder", "id", "label", "type", "name", "text", "src"]
    for _element in elements:
        for _attribute in attributeList:
            if _element.get_attribute(_attribute) == identifier:
                if not property:
                    best.add(_element)
                else:
                    if _element.get_property(property[0]) == property[1]:
                        best.add(_element)
        if elementType == "button":
            if _element.text == identifier:
                best.add(_element)
    if len(best) < 1:
        return False
    else:
        return best.pop()
