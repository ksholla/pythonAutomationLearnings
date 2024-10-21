from selenium import webdriver
from selenium.webdriver.common.by import By

#Chrome browser
driver = webdriver.Chrome()

#Page URL
driver.get("https://awesomeqa.com/ui/index.php?route=account/register")

#<input type="text"
# name="firstname"

first_name_input = driver.find_element(By.NAME, "firstname")
first_name_input.send_keys("Test")

##<input type="text" name="lastname" value="" placeholder="Last Name" id="input-lastname" class="form-control">
last_name_input = driver.find_element(By.NAME, "lastname")
last_name_input.send_keys("User")

##<input type="email" name="email" value="" placeholder="E-Mail" id="input-email" class="form-control">
email_input = driver.find_element(By.NAME, "email")
email_input.send_keys("Testuser@gmail.com")

##<input type="tel" name="telephone" value="" placeholder="Telephone" id="input-telephone" class="form-control">
telephone_input = driver.find_element(By.NAME, "telephone")
telephone_input.send_keys("9900123456")

##<input type="password" name="password" value="" placeholder="Password" id="input-password" class="form-control">
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys("Test@123")

##<input type="password" name="confirm" value="" placeholder="Password Confirm" id="input-confirm" class="form-control">
password_confirm_input = driver.find_element(By.NAME, "confirm")
password_confirm_input.send_keys("Test@123")

## skipping newsletter option

#<input type="checkbox" name="agree" value="1">
privacy_policy_checkbox = driver.find_element(By.NAME, "agree")
privacy_policy_checkbox.click()

# <input type="submit" value="Continue" class="btn btn-primary">
continue_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Continue']")
continue_button.click()

driver.implicitly_wait(5)

#<a href="https://awesomeqa.com/ui/index.php?route=account/account" class="btn btn-primary">Continue</a>
Continue_btn = driver.find_element(By.CLASS_NAME,"btn btn-primary")
continue_button.click()

driver.implicitly_wait(5)
# Optionally, you can print a message indicating the success of the test
print("Test passed.")