import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://awesomeqa.com/webtable.html")
driver.maximize_window()

company = driver.find_element(By.XPATH, "//td[text()='Helen Bennett']/preceding-sibling::td[1]").text
country = driver.find_element(By.XPATH, "//td[text()='Helen Bennett']/following-sibling::td[1]").text
print(company, 'and ',country)