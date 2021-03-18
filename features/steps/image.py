from behave import *
from PIL import Image, ImageChops
from datetime import *
from os import path

@then(u'the screenshot matches the golden image "{filename}"')
def compare_screenshot(context, filename):
    def _convert(screenshotPath):
        screenshot = Image.open("%s" %(screenshotPath))
        screenshot = screenshot.convert("RGB")
        f, e = path.splitext(screenshotPath)
        outfile = f + ".jpg"
        screenshot.save(outfile)
        return outfile

    screenshotPath = "%s/%s.png" %(context.browser.scratch, datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))
    screenshot = context.browser.browser.save_screenshot("%s" %(screenshotPath))
    golden = Image.open("images/%s" %(filename))
    screenshot = Image.open(_convert(screenshotPath))
    diff = ImageChops.difference(golden, screenshot)
    if diff.getbbox():
        print("%s differs from the golden image!" %(screenshotPath))
        return False
    else:
        return True
