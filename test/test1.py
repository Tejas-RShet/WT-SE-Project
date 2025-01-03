from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def test_signup_page():
    service = Service(executable_path="C:\\Users\\Tejas\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    try:
        driver.get("http://localhost:3000/signup")

        # Ensure the file path is valid
        image_path = "C:\\Users\\Tejas\\OneDrive\\Attachments\\Desktop\\logo.png"
        if not os.path.exists(image_path):
            print("Image file not found.")
            return

        # Locate the visible 'Upload' button and click it
        upload_button = driver.find_element(By.CSS_SELECTOR, "div.absolute.bottom-0.h-1\\/3.bg-slate-500")
        ActionChains(driver).move_to_element(upload_button).click().perform()

        # Find the hidden file input and upload the image
        file_input = driver.find_element(By.ID, "profileImage")
        file_input.send_keys(image_path)
        print("Image uploaded successfully.")

        # Fill out other fields in the signup form
        driver.find_element(By.NAME, "firstName").send_keys("John")
        driver.find_element(By.NAME, "lastName").send_keys("Doe")
        driver.find_element(By.NAME, "email").send_keys("jhonndoe@gmail.com")
        driver.find_element(By.NAME, "password").send_keys("TestPassword123")
        driver.find_element(By.NAME, "confirmPassword").send_keys("TestPassword123")

        # Locate and click the signup button
        signup_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign up')]"))
        )
        signup_button.click()

        # Wait for a response message and print it
        message_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "p"))
        )
        print(f"Signup result: {message_element.text}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_signup_page()
