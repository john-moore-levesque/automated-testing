For more information about Behave steps, look at https://behave.readthedocs.io/en/stable/tutorial.html#feature-files

# When
Per the documentation, `When` statements take specified actions that should cause some state to change.
- `When we go to "{url}"` - go to the specified url
- `When we wait` - wait for 5 seconds
- `When we wait {n} seconds` - wait for the specified number of seconds
- `When we clear cache` - clear the browser cache
- `When we click on the link called "{link}"` - click on a link with the displayed text
- `When we select "{option}" from the dropdown "{dropdown}"` - select the option from the specified dropdown
- `When we click {extraText} {fieldType} {fillerText} "{thingToClick}"` - click on thingToClick, with some extra text for filler words (e.g., "on", "the", "a") and a field type (input field, checkbox, etc). The helper function `getElement` is used to find page elements of the specified type, and then the `thingToClick` value is compared against the following list of attributes:
  - title
  - value
  - placeholder
  - id
  - label
  - type
  - name
  - text
  - src
  - for
  - class
- `When we click the "{button}" button` - specifically click on something of the "button" type
- `When we click on the "{checkbox}" checkbox` - specifically click on something of the "checkbox" type
- `When we put "{text}" into the "{field}" field` - put text into a specified field
- `When we select the radio button marked "{radiotext}"` - click on a radio button
- `When we switch to "{frame}"` - switch to a specified frame
- `When we switch to the main body` - switch (back) to the main body
- `When we hit enter in the field "{field}"` - go to the specified field and hit "Enter"

# Given
Per the documentation, `Given` statements force a known state before the user interacts with the system.
- `Given we go to "{url}"` - go to the specified URL
- `Given we switch to "{frame}"` - switch to a specified frame
- `Given we switch to the main body` - switch (back) to the main body
- `Given we wait` - wait for 5 seconds
- `Given we wait {n} seconds` - wait for the specified number of seconds

# Then
Per the documentation, `Then` statements observe outcomes and compare the outcomes to expectations.
- `Then it says "{testString}"` - check to see if testString is in the page source
- `Then it does NOT say "{testString}"` - check to see if testString is NOT in the page source
- `Then it says either "{testString1}" or "{testString2}"` - check to see if either testString1 or testString2 appear in the page source
- `Then the title is "{title}"` - check to see that the `title` tag matches the specified value
- `Then the current URL is "{currentUrl}"` - check the current URL; this is helpful for testing redirection
- `Then the current URL contains "{currentUrl}"` - check that the current URL contains a specific string; this is helpful if the current URL has a known "base", but also contains a session ID or hash or something like that
- `Then it has an image with the source "{source}"` - check to see if there's an `img` element with the specified `src` value
- `Then it has a {thing} with the {identifier} "{thingname}"` - check to see if there's a thing with the attribute thingName. For instance, `Then it should have a CSS element with the class "foo"`
