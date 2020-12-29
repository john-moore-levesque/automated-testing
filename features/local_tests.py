from local_settings import checkFirefox, checkChrome, load_env
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


def createBrowser():
    load_env()
    chrome = checkChrome()
    firefox = checkFirefox()
    if chrome:
        return Chrome()
    elif firefox:
        return Firefox()
    else:
        return False
