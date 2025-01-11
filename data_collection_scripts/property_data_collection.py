from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import json

# Define the Domain.com URL for the property
url = "https://www.domain.com.au/25-cross-street-strathfield-nsw-2135-2019633454"

# Setup WebDriver
CHROME_DRIVER_PATH = "chromedriver.exe"
service = Service(CHROME_DRIVER_PATH)

# Function to scrape data for a property using Domain.com
def scrape_property(driver, url):
    driver.get(url)
    time.sleep(2)
    property_data = {}

    try:
        # Title
        title = driver.find_element(By.CLASS_NAME, "css-twgrok").text
        
        # Extracting Type of Sale and Price
        type_price = title.split(" | ")
        property_data["Type of Sale"] = type_price[0]
        property_data["Price"] = type_price[1]

        # Extracting all amentities values
        parent_element = driver.find_element(By.CLASS_NAME, "css-1dtnjt5")
        details = parent_element.find_elements(By.CLASS_NAME, "css-1ie6g1l")
        for detail in details:
            value_label = detail.find_element(By.CLASS_NAME, "css-lvv8is").text
            value_label_pair = value_label.split("\n")
            property_data[value_label_pair[1]] = value_label_pair[0]

        # Brief Description
        brief_description = driver.find_element(By.CLASS_NAME, "css-juce83").text
        property_data["Headline"] = brief_description

        # Detailed Description
        description_element = driver.find_element(By.CLASS_NAME, "css-bq4jj8")
        descriptions = description_element.find_elements("css selector", "p")
        property_data["Summary Description"] = "\n".join([x.text for x in descriptions])
    except Exception as e:
        print(f"Error extracting data: {e}")

    return property_data

def collect_property_data():
    driver = webdriver.Chrome(service=service)
    property_data = scrape_property(driver, url)
    driver.quit()

    if property_data:
        output_file = "property_data.txt"
        with open(output_file, "w") as f:
            f.write(json.dumps(property_data))
        print(f"Data saved to {output_file}")
    else:
        print("No property data found.")
