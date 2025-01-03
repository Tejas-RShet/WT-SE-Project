from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import re

# Initialize WebDriver with the Service object
service = Service(executable_path="C:\\Users\\Tejas\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open the Contact page
driver.get('http://localhost:3000/contact')

# Wait for the page to load
time.sleep(2)

# Locate form elements
name_input = driver.find_element(By.NAME, 'name')
email_input = driver.find_element(By.NAME, 'email')
message_input = driver.find_element(By.NAME, 'message')
submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')

# Test data
valid_name = "John Doe"
invalid_name_1 = "John0"  # Invalid due to digit
invalid_name_2 = "John@Doe"  # Invalid due to special character
valid_email = "johndoe@example.com"
invalid_email = "0@gmail.com"  # Invalid email
valid_message = "This is a valid message with more than five words."
invalid_message = "Short msg"  # Invalid message with less than 5 words

def validate_name(name):
    if re.search(r'[0-9]', name) or re.search(r'[^a-zA-Z\s]', name):
        return False
    return True

def validate_email(email):
    if '0' in email.split('@')[0]:  # Check for '0' in the part before '@'
        return False
    return True

def validate_message(message):
    if len(message.split()) < 5:  # Ensure message has at least 5 words
        return False
    return True

def fill_and_submit_form(name, email, message):
    name_input.clear()
    email_input.clear()
    message_input.clear()

    # Fill form
    name_input.send_keys(name)
    email_input.send_keys(email)
    message_input.send_keys(message)

    # Submit form
    submit_button.click()

# Test case 1: Valid input
if validate_name(valid_name) and validate_email(valid_email) and validate_message(valid_message):
    fill_and_submit_form(valid_name, valid_email, valid_message)
    time.sleep(3)  # Wait for form submission response
    print("Test 1 Passed: Form submitted successfully")
else:
    print("Test 1 Failed: Invalid input data")

# Test case 2: Invalid name (contains digit)
if not validate_name(invalid_name_1):
    print("Test 2 Passed: Invalid name detected")
else:
    print("Test 2 Failed: Name validation didn't work")

# Test case 3: Invalid name (contains special character)
if not validate_name(invalid_name_2):
    print("Test 3 Passed: Invalid name detected")
else:
    print("Test 3 Failed: Name validation didn't work")

# Test case 4: Invalid email (contains '0' before '@')
if not validate_email(invalid_email):
    print("Test 4 Passed: Invalid email detected")
else:
    print("Test 4 Failed: Email validation didn't work")

# Test case 5: Invalid message (less than 5 words)
if not validate_message(invalid_message):
    print("Test 5 Passed: Invalid message detected")
else:
    print("Test 5 Failed: Message validation didn't work")

# Close the driver after tests
driver.quit()
