import time
from selenium 							import webdriver
from selenium.webdriver.chrome.options 	import Options
from selenium.common.exceptions 		import WebDriverException

#Interface
iterationNumber = int(input("Enter the number of iterations: "))

#Variables
userDataDir 	= '/Users/Jeca22/Library/Application Support/Google/Chrome/Profile 1'
executablePath 	= '/Users/Jeca22/Desktop/pythonTest/chromedriver'

#Options 
chromeOptions = Options()
chromeOptions.add_argument('user-data-dir='+userDataDir)
chromeOptions.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])

#Driver initialization
driver = webdriver.Chrome(executable_path=executablePath,chrome_options=chromeOptions)

#Start process
i = 0
while(i < iterationNumber):
	driver.get('https://www.linkedin.com/people/pymk/hub?ref=global-nav&trk=nav_utilities_pymk_header')
	
	#We need to refresh the page because after the click, the css selector changes it name
	#it could be done in different ways but this is the most affordable one 
	
	connectButtons = driver.find_elements_by_css_selector('button.bt-request-buffed.buffed-blue-bkg-1')
	connectButtonsSize = len(connectButtons)-1

	for j in range(1,connectButtonsSize):
		currentButton = connectButtons[j]	
		try:
			currentButton.click()	
			time.sleep(6) #based on speed test done with free tools
		except Exception as e:
			print e
	i = i + 1

driver.close()
