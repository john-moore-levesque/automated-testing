from os import environ, stat
from dotenv import load_dotenv
from local_settings import authInformation, checkFirefox, checkChrome
from chrome import Browser as Chrome
from firefox import Browser as Firefox

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
