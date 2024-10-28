import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Open the MakeMyTrip website
driver.get("https://www.makemytrip.com")

# Wait for the popup to appear and close it
try:
    popup = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@data-cy='close']"))
    )
    popup.click()
except Exception as e:
    print("Popup not found or already closed:", e)

# Continue with additional actions if needed
# For example, interacting with other fields on the page
