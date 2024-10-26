from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the eBay Desktops & All-In-One Computers page
driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")

#Mini mac
#<input type="text" class="gh-tb ui-autocomplete-input" aria-autocomplete="list" aria-expanded="false" size="50"
# maxlength="300" aria-label="Search for anything" placeholder="Search for anything"
# id="gh-ac" name="_nkw" autocapitalize="off" autocorrect="off" spellcheck="false"
# autocomplete="off" value="macmini" aria-haspopup="true" role="combobox" aria-owns="ui-id-1">
search_text = driver.find_element(By.ID, "gh-ac")


search_text.send_keys("mac mini")

#search 
search_btn = driver.find_element(By.ID, "gh-btn")
search_btn.click()

# Retrieve the list of items
list_of_items = driver.find_elements(By.CSS_SELECTOR, ".s-item__title")

# Print the title of each item
for item in list_of_items:
    print(item.text)

# Close the browser
driver.quit()
