from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# Open the eBay Desktops & All-In-One Computers page
driver.get("https://awesomeqa.com/practice.html")

firstname = driver.find_element(By.XPATH, "//input[@name='firstname']")
firstname.send_keys("mac mini")

actions = ActionChains(driver=driver)
(actions
 .key_down(Keys.SHIFT)
 .send_keys_to_element(firstname,"the testing acadamy")
 .key_up(Keys.SHIFT).perform()
 )