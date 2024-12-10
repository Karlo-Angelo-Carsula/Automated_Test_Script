from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager  # This will help manage ChromeDriver automatically
import time

# Function to validate the fields in the form
def validate_fields(driver):
    try:
        # Name field validation
        name_field = driver.find_element(By.ID, "name")
        name_field.clear()
        name_field.send_keys("Micheal Escosio")  # Enter a valid name
        assert len(name_field.get_attribute("value")) <= 100, "Name exceeds max length!"

        # Photo field validation
        photo_field = driver.find_element(By.ID, "photo")
        # No actual file upload, just checking that the field exists
        assert photo_field.is_displayed(), "Photo upload field is missing!"

        # Description field validation
        description_field = driver.find_element(By.ID, "description")
        description_field.clear()
        description_field.send_keys("This is a sample description for testing the validation.")  # Valid description
        assert len(description_field.get_attribute("value")) <= 10000, "Description exceeds max length!"

        # Business Type field validation
        business_type_field = Select(driver.find_element(By.ID, "businessType"))
        business_type_field.select_by_visible_text("Retail")  # Selecting an option from the dropdown
        assert business_type_field.first_selected_option.text == "Retail", "Business Type not selected correctly!"

        # Contact Person Name field validation
        contact_name_field = driver.find_element(By.ID, "contactName")
        contact_name_field.clear()
        contact_name_field.send_keys("Micheal Escosio")  # Enter a valid name
        assert len(contact_name_field.get_attribute("value")) <= 100, "Contact Person Name exceeds max length!"

        # Contact Person Phone Number field validation
        contact_phone_field = driver.find_element(By.ID, "contactPhone")
        contact_phone_field.clear()
        contact_phone_field.send_keys("09661578552")  # Enter a valid phone number
        assert len(contact_phone_field.get_attribute("value")) <= 15, "Phone Number exceeds max length!"
        
        print("All fields validated successfully!")

    except AssertionError as e:
        print(f"Validation failed: {e}")
    except Exception as e:
        print(f"Error: {e}")

# Setup WebDriver (Chrome) using Service
service = Service(executable_path="C:\\Users\\Gelo\\Desktop\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe") 
driver = webdriver.Chrome(service=service)

# Open the HTML file (use a local path or URL)
driver.get("file:///C:/Users/Gelo/test.html")

# Validate fields
validate_fields(driver)

# Wait for a few seconds to review results
time.sleep(5)

# Close the browser
driver.quit()
