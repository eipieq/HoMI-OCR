# Sanskrit OCR Automation

This Python script utilizes the Selenium WebDriver to automate the process of extracting text from images using the OCR service provided by [https://ocr.sanskritdictionary.com](https://ocr.sanskritdictionary.com). The script is designed to work with the Firefox browser.

## Prerequisites
- Ensure you have the appropriate [GeckoDriver](https://github.com/mozilla/geckodriver) executable for your operating system. Download the executable and rename it according to your system: `geckodriver_mac` for macOS, `geckodriver_linux` for Linux, or `geckodriver_windows.exe` for Windows.

## Dependencies
- This script relies on the Selenium library. If you don't have it installed, you can install it using:
  ```
  pip install selenium
  ```

## Usage
1. Place the images in the HoMI-OCR directory containing the script and driver files.
2. Run the script.

## Description
1. The script opens the OCR service page in the Firefox browser.
2. It uses JavaScript to click the hidden file input and uploads an image file.
3. After uploading the image, it waits for a period (simulated using `time.sleep`) to allow the OCR service to process the image. In a production scenario, waiting for a specific element indicating completion is recommended.
4. It switches to the result iframe and extracts the text from the `<p>` tag containing the OCR result.
5. The extracted text is written to a text file (`ocr_result{page_number}.txt`) for each processed page.

## Note
- This script is a basic example and may require adjustments based on changes to the OCR service or web page structure.
- Always comply with the terms of service of the OCR service you are using.

Feel free to modify the script according to your specific requirements and ensure that you comply with the terms and conditions of the OCR service you are interacting with.

## Credits
The program was created in partnership with [Shubham Gupta](https://github.com/brainspoof).

This script and the program was assisted by [ChatGPT](https://www.openai.com/), a product of OpenAI.
