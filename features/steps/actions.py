from behave import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

def getElement(context, elementType, identifier, property=False):
    elements = context.browser.browser.find_elements_by_tag_name("%s" %(elementType))
    best = set()
    attributeList = ["title", "value", "placeholder", "id", "label", "type", "name", "text", "src", "for"]
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

# Click on a radio button
@when(u'we select a radio button marked "{radiotext}"')
def step_impl(context, radiotext):
    myRadio = getElement(context, "input", radiotext, ("type", "radio"))
    if myRadio:
        myRadio.click()
    else:
        return False

# Click a checkbox
@when(u'we click on the "{checkbox}" checkbox')
def step_impl(context, checkbox):
    myCheckbox = getElement(context, "input", checkbox, ("type", "checkbox"))
    if myCheckbox:
        myCheckbox.click()
    else:
        return False

# Click on a link
@when(u'we click on a link called "{link}"')
@given(u'we click on a link called "{link}"')
def step_impl(context, link):
    myLink = context.browser.browser.find_element_by_link_text(link)
    if myLink:
        myLink.click()
    else:
        return False

# Put text into a field
@when(u'we put "{text}" into "{field}"')
@when(u'we put "{text}" into the "{field}" field')
@given(u'we put "{text}" into "{field}"')
@given(u'we put "{text}" into the "{field}" field')
def step_impl(context, text, field):
    inputField = getElement(context, "input", field)
    try:
        inputField.send_keys(text)
    except AttributeError:
        return False

# Hit enter in a field
@when(u'we hit enter in the field "{field}"')
@when(u'we hit enter in the "{field}" field')
def step_impl(context, field):
    inputField = getElement(context, "input", field)
    try:
        inputField.send_keys(Keys.ENTER)
    except AttributeError:
        return False

# Click on something
@when(u'we click {extraText} {fieldType} {fillerText} "{button}"')
@given(u'we click {extraText} {fieldType} {fillerText} "{button}"')
def step_impl(context, extraText, fieldType, fillerText, button):
    fieldToClick = getElement(context, fieldType, button)
    if fieldToClick:
        fieldToClick.click()
        return True
    else:
        return False

# Click on a button (specifically)
@when(u'we click the "{button}" button')
def step_impl(context, button):
    buttonToClick = getElement(context, "button", button)
    if buttonToClick:
        buttonToClick.click()
        return True
    else:
        return False

# Check for downloaded file
@then(u'there should be a downloaded file named "{filename}"')
def step_impl(context, filename):
    assert context.browser.statfile(filename)


# Check for a partial downloaded filename
@then(u'there should be a downloaded file that contains "{filename}"')
def step_impl(context, filename):
    assert context.browser.statfile(filename, partial=True)

# Select from a dropdown
@when(u'we select "{option}" from the "{dropdown}" dropdown')
@when(u'we select "{option}" from the dropdown "{dropdown}"')
@given(u'we select "{option}" from the "{dropdown}" dropdown')
@given(u'we select "{option}" from the dropdown "{dropdown}"')
def step_impl(context, option, dropdown):
    myDropdown = Select(getElement(context, "select", dropdown))
    if myDropdown:
        myDropdown.select_by_visible_text(option)
        return True
    return False


# Clear cookies
@when(u'we clear the cache')
@when(u'we clear cache')
def step_impl(context):
    context.browser.clearCache()

# Wait 5 seconds (default)
@when(u'we wait')
@given(u'we wait')
def step_impl(context):
    context.browser.wait()

@when(u'we wait {n} seconds')
@given(u'we wait {n} seconds')
def step_impl(context, n):
    try:
        n = int(n)
    except ValueError:
        n = 5
    context.browser.wait(n)
