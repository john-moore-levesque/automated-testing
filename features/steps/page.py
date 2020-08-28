from behave import *

# Check the page title
@given(u'the title is "{title}"')
@then(u'the title should be "{title}"')
def step_impl(context, title):
    try:
        assert context.browser.browser.title == title
    except AssertionError:
        return False


# Check the page source for a testString
@given(u'it says "{testString}"')
@then(u'it should include "{testString}"')
@then(u'it should say "{testString}"')
def step_impl(context, testString):
    try:
        assert testString in context.browser.browser.page_source
    except AssertionError:
        return False


# Check the page source for one of two possible test strings
@given(u'it says either "{testString1}" or "{testString2}"')
@then(u'it should include either "{testString1}" or "{testString2}"')
@then(u'it should say either "{testString1}" or "{testString2}"')
def step_impl(context, testString1, testString2):
    try:
        assert testString1 in context.browser.browser.page_source or testString2 in context.browser.browser.page_source
    except AssertionError:
        return False


# Check the page source for the ABSENCE of a testString
@then(u'it should NOT include "{testString}"')
@then(u'it should NOT say "{testString}"')
def step_impl(context, testString):
    try:
        assert testString not in context.browser.browser.page_source
    except AssertionError:
        return False

# Check for an element in the page
@then(u'it should have a {thing} with the {identifier} "{thingname}"')
def step_impl(context, thing, identifier, thingname):
    if "tag" in identifier.lower():
        assert context.browser.browser.find_elements_by_tag_name(thingname)
    elif "class" in identifier.lower():
        assert context.browser.browser.find_elements_by_class_name(thingname)
    elif "name" in identifier.lower():
        assert context.browser.browser.find_element_by_name(thingname)
    elif "xpath" in identifier.lower():
        assert context.browser.browser.find_element_by_xpath(thingname)
    else:
        assert context.browser.browser.find_element_by_id(thingname)
