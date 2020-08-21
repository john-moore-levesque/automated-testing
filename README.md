# automated-testing

Automated testing framework using Behave, Python, and Selenium.

## Pre-Requisites
* Python 3.6+
* VirtualEnv 15.2.1+
* The Selenium ChromeDriver, downloaded and installed in the selenium-drivers directory

Python, VirtualEnv, and the Selenium ChromeDriver must be available on your user's path.

## Installation
This assumes that you have cloned the repo into /path/to/repo (or CL\path\to\repo, for Windows)

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

# More Information
* Selenium ChromeDriver: https://chromedriver.chromium.org/downloads
* Behave: https://behave.readthedocs.io/en/latest/
