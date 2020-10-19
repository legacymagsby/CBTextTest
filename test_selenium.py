from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os

username = os.getenv("CBT_USERNAME")
access_key = os.getenv("CBT_AUTHKEY")


caps = {
 'platform': 'Windows',
 'browserName': 'chrome',
}

driver = webdriver.Remote(
    command_executor="http://%s:%s@hub.crossbrowsertesting.com/wd/hub"%(username, access_key),
    desired_capabilities=caps)



driver.get("http://www.google.com")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
elem = driver.find_element_by_name("q")
elem.send_keys("CrossBrowserTesting")
elem.submit()
print(driver.title)
driver.quit()
