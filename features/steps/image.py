from behave import *
from PIL import Image, ImageChops
from datetime import *


@then(u'the screenshot matches the golden image "{filename}"')
def compare_screeshot(context, filename):
    screenshotPath = "%s/%s.png" %(context.browser.scratch, datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))
    screenshot = context.browser.browser.save_screenshot("%s" %(screenshotPath))
    golden = Image.open("images/%s" %(filename))
    screenshot = Image.open("%s" %(screenshotPath))
    diff = ImageChops.difference(golden, screenshot)
    if diff.getbbox():
        print("%s differs from the golden image!" %(screenshotPath))
        return False
    else:
        return True
