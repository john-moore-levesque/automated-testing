# automated-testing

Automated testing framework using Behave, Python, and Selenium.

## Pre-Requisites
* Python 3.6+
* VirtualEnv 15.2.1+
* The Selenium ChromeDriver, downloaded and installed in the selenium-drivers directory
* The Gecko driver (for Firefox), downloaded and installed in the selenium-drivers directory

Note that you do not need both drivers, just one.

Python, VirtualEnv, and the Selenium ChromeDriver (or the Gecko driver) must be available on your user's path.

## Installation
This assumes that you have cloned the repo into /path/to/repo (or C:\path\to\repo, for Windows)

### Windows
<pre>
cd C:\path\to\repo
virtualenv.exe venv
.\venv\Scripts\activate
(venv) pip install -r requirement.txt
</pre>

### Linux
<pre>
cd /path/to/repo
virtualenv venv
source venv/bin/activate
(venv) pip install -r requirement.txt
</pre>

Additionally, if you are using Firefox on Linux you will need to make sure you have:
* gtk3
* libXt

(Note that the above was specifically written regarding CentOS - your mileage may vary with other distros.)

### local_settings.py
Copy the features/local_settings.py.example file to features/local_settings.py and edit as appropriate.

## Usage

### Running Tests
To run tests, first create feature files in /path/to/repo/features/.

Once you have feature files, on Windows:
<pre>
cd C:\path\to\repo
.\venv\Scripts\activate
(venv) cd features
(venv) behave -i filename.feature
</pre>

On Linux:
<pre>
cd /path/to/repo
source venv/bin/activate
(venv) cd features
(venv) behave -i filename.feature
</pre>

# Why Not behave-webdriver?
No disrespect to the developers of behave-webdriver (https://pypi.org/project/behave-webdriver/), but I found that for my purposes, it was just too limited. In particular, my goal was to create a test suite that *didn't* require you to use the full XPATH, or the exact CSS properties. Rather, I wanted something where anyone could look at a rendered webpage in their browser, see a button called "Click me!" and write a test that would click the "Click me!" button.

When I was reviewing the behave-webdriver documentation and source code, and experimenting with how to use it, I kept getting stymied by the fact that I was able to look at the rendered web page, see the "Click me!" button, and *not* be able to click it without having to go through a lot of hoops.

# Writing Tests
* [Available Tests](docs/available-tests.md)
* [Simple Tests](docs/simple.md)

# More Information
* Selenium ChromeDriver: https://chromedriver.chromium.org/downloads
* Gecko driver: https://github.com/mozilla/geckodriver/releases
* Behave: https://behave.readthedocs.io/en/latest/
