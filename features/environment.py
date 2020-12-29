from chrome import before_all as chromeBrowser
from firefox import before_all as firefoxBrowser
from local_settings import checkChrome, checkFirefox, load_env


def before_all(context):
    '''
    If "chrome" is true, then a Chrome browser will be created
    If "firefox" is true, a Firefox browser will be created
    Otherwise it returns False
    '''
    load_env()
    chrome = checkChrome()
    firefox = checkFirefox()
    if chrome:
        chromeBrowser(context)
    elif firefox:
        firefoxBrowser(context)
    else:
        return False
