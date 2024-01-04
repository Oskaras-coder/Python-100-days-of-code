from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

pattern = r'\d{1,3}(?:,\d{3})*(?:\.\d+)?'

store = driver.find_elements(By.CSS_SELECTOR, value="#store b")[:-1]
prices = []

items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

for product in store:
    price = re.findall(pattern, product.text)
    store_price = int(price[0].replace(',', ''))
    prices.append(store_price)
new_prices = prices[::-1]

start_time = time.time()
duration = 300
interval = 5

while True:
    # Your code goes here
    cookie.click()
    money = int(driver.find_element(By.ID, value="money").text.replace(",", ""))

    if time.time() - start_time >= interval:
        # Add your code that needs to be executed every 5 seconds here
        for cost in new_prices:
            if cost <= money:
                index = prices.index(cost)
                driver.find_element(By.ID, value=item_ids[index]).click()
                break
        # Reset the timer for the next interval
        start_time = time.time()

    # Calculate elapsed time
    elapsed_time = time.time() - start_time

    # Check if the elapsed time has reached the desired duration
    if elapsed_time >= duration:
        break  # Exit the loop after the specified duration

    time.sleep(0.1)  # Adjust the sleep duration as needed
