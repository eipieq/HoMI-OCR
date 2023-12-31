from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the Selenium WebDriver with the service
service = Service('/Users/zap/Documents/Work/CCL/HoMI-OCR/geckodriver')

# Loop for 3 pages
for page_number in range(1, 4):
    driver = webdriver.Firefox(service=service)

    try:
        # Open the OCR service page
        driver.get('https://ocr.sanskritdictionary.com')

        # Use JavaScript to click the hidden file input
        driver.execute_script("document.getElementById('pictureFile').click();")

        # Wait for the file input to become available and send the file path
        wait = WebDriverWait(driver, 10)
        file_input = wait.until(EC.presence_of_element_located((By.ID, 'pictureFile')))
        file_input.send_keys(f'/Users/zap/Documents/Work/CCL/HoMI-OCR/image{page_number}.jpg')

        # Wait for some time to let the OCR process the image
        # In a real-world scenario, you should wait for a specific element that indicates the process is complete
        time.sleep(15)

        # The result is within an iframe, so we switch to the iframe
        iframe = driver.find_element(By.CSS_SELECTOR, '#tinymcetext_ifr')
        driver.switch_to.frame(iframe)

        # Now get the text from the <p> tag which contains the result
        result_text = driver.find_element(By.TAG_NAME, 'p').text

        # Switch back to the main document
        driver.switch_to.default_content()

        # Write the result text to a file
        with open(f'/Users/zap/Documents/Work/CCL/HoMI-OCR/ocr_result{page_number}.txt', 'w') as file:
            file.write(result_text)

    finally:
        # Close the browser
        driver.quit()