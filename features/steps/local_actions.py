from behave import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

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
