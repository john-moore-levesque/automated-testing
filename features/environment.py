from local_settings import checkChrome, checkFirefox
import behave_webdriver


def before_all(context):
    # If "chrome" is true, then a Chrome browser will be created
    # If "firefox" is true, a Firefox browser will be created
    # Otherwise it returns False
    chrome = checkChrome()
    firefox = checkFirefox()
    if chrome:
        context.behave_driver = behave_webdriver.Chrome.headless()
    elif firefox:
        context.behave_driver = behave_webdriver.Firefox.headless()
    else:
        return False


def after_all(context):
    context.behave_driver.quit()

# def before_all(context):
#     context.behave_driver = behave_webdriver.Firefox.headless()
#
# def after_all(context):
#     context.behave_driver.quit()
