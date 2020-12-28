# Writing a simple test
Follow these rough steps to create your own test. Feature files are intented to behuman-readable and functional, so don't worry about *how* something happens - just say what needs to happen.

## First steps
First, create a file in the "features" directory called "mytest.feature".

```
Feature: My Test Plan
```

## Create a scenario
Each test unit is called a "Scenario". It is not required to have a tag (prefaced by the "@" sign), but it's helpful for keeping things organized.

```
Feature: My Test Plan

@my.test
Scenario: test www.example.com
```

## Go to the page
First things first - you need to go to a page.

```
Feature: My Test Plan

@my.test
Scenario: test www.example.com
When we go to "http://www.example.com"
```

## Check to see if something is on the page
The simplest thing to do is check to see if there is some test string in the page source. Note that this is case-sensative. Note also that you can be led astray by HTML tags. That is, if you're looking for "Hello there!", it will FAIL if the text in the source is actually <code><h1>Hello</h1> there!</code>.

```
Feature: My Test Plan

@my.test
Scenario: test www.example.com
When we go to "http://www.example.com"
Then it says "Example Domain"
```

## Check to see if something is NOT on the page
You can also check to see if something is NOT on the page (e.g., "Database Error!"). The same caveat about HTML tags applies here.

```
Feature: My Test Plan

@my.test
Scenario: test www.example.com
When we go to "http://www.example.com"
Then it says "Example Domain"
Then it does NOT say "Database Error!"
```

## Check the page title
It can also be helpful to check the HTML <code>title</code> attribute.

```
Feature: My Test Plan

@my.test
Scenario: test www.example.com
When we go to "http://www.example.com"
Then it says "Example Domain"
Then it does NOT say "Database Error!"
Then the title is "Example Domain"
```

## Check for a redirect
If you want to see if you get redirected when you go to a page, you can check the current url.
```
Feature: My Other Test Plan

@my.other-test
Scenario: see if https://www.iana.org/domains/example redirects
When we go to "https://www.iana.org/domains/example"
Then the current URL is "https://www.iana.org/domains/reserved"
Then it says "IANA-managed Reserved Domains"
```

# Available Tests
If you have any questions about what tests are supported, review the list of [available tests](available-tests.md).

I have done my best to make sure that you can just go off of what you see on the screen, rather than having to delve into the Chrome Developer Tools panel, but sometimes that's just unavoidable. As an example, if you are trying to click on something that *should* just be a radio button, but Selenium insists it can't find the element, look at the page source and try clicking on the CSS div or label instead.
