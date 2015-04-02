# Web Tools
Some multiplatform tools to automate growth of users in different communities. 

Everything is programmed using Python 3.4.3, Selenium and the Chrome web driver.
You need to include selenium once you have installed python in your computer, you just need to 
execute *pip install selenium*
Once you have it installed you need to download the chrome web driver from https://sites.google.com/a/chromium.org/chromedriver/downloads

With the script linkedin_contacts_growth.py you can automate the task of adding connections.
First you need to execute the web driver from the python idle for example and introduce your LinkedIn account.
It will be saved in your profile created for this session. (f it is the fisr time you use the web driver it will be Profile 1)

After that, you need to specify two parameter:
userDataDir is where your profile is, use the path in the example to find your own profile in your system. 

```userDataDir 	  = '/Users/Jeca22/Library/Application Support/Google/Chrome/Profile 1'```

executablePath is where the webdriver you just downloaded is storaged. You need to give the path where it is. 
I recommend to put it in the same folder than your scripts.

```executablePath 	= '/Users/Jeca22/Desktop/pythonTest/chromedriver'```
