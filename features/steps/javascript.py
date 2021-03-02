from behave import *

@when(u'we trigger the JavaScript "{script}"')
def triggerJS(context, script):
    context.browser.browser.execute_script(script)

@when(u'we put "{text}" into the field with the ID "{field}" using JavaScript')
def jsTextId(context, field, text):
    context.browser.browser.execute_script("document.getElementById('%s').setAttribute('value', '%s')" %(field, text))

@when(u'we put "{text}" into the field with the class "{field}" using JavaScript')
def jsTextClass(context, field, text):
    context.browser.browser.execute_script("document.getElementsByClassName('%s')[0].setAttribute('value', '%s')" %(field, text))

@when(u'we click on something with the ID "{thing}" using JavaScript')
def jsClickId(context, thing):
    context.browser.browser.execute_script("document.getElementById('%s').click()" %(thing))

@when(u'we click on something with the class "{thing}" using JavaScript')
def jsClickId(context, thing):
    context.browser.browser.execute_script("document.getElementsByClassName('%s')[0].click()" %(thing))

@when(u'we make "{element}" disappear with JavaScript')
def jsDisappear(context, element):
    context.browser.browser.execute_script("document.getElementById('%s').style.display = 'none'" %(element))
