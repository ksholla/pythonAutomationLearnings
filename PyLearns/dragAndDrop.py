import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

driver.maximize_window()

drag_item = driver.find_element(By.ID,"draggable")
drop_item = driver.find_element(By.ID,"droppable")
time.sleep(4)
actions = ActionChains(driver)
actions.drag_and_drop(drag_item,drop_item).perform()

