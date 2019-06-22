from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("..\Driver\chromedriver.exe")
# driver = webdriver.Ie("..\Driver\IEDriverServer.exe")

driver.set_page_load_timeout(10)
driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("Belajar Automented")
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)

driver.maximize_window()
driver.refresh()

print("Test Sudah Completed")