from behave import *

# Go to a specified URL
@when(u'we go to "{url}"')
@given(u'we go to "{url}"')
def step_impl(context, url):
    context.browser.browser.get(url)


# Check the current url
@then(u'the current URL is "{currentUrl}"')
def step_impl(context, currentUrl):
    assert context.browser.browser.current_url == currentUrl


# Partial URL match (useful if you have a URL that contains a session ID)
@then(u'the current URL contains "{currentUrl}"')
def step_impl(context, currentUrl):
    assert currentUrl in context.browser.browser.current_url
