import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By

import time

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
FORM_URL = "https://forms.gle/eBG9pdrCrcNQ2EcD6"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537."
    "36 (KHTML, like Gecko) Chrome/119.0.0.0 "
    "Safari/537.36",
    "Accept-Language": "lt-LT,lt;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,pl;q=0.5",
}

response = requests.get(ZILLOW_URL, headers=header)
soup = BeautifulSoup(response.text, "lxml")

list_of_urls = soup.find_all("a", class_="property-card-link")
url_list = [link["href"] for link in list_of_urls]
# print(list_of_urls)

prices_list = soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")
prices = [
    price.getText().split("+")[0].split("/")[0].replace(",", "")
    for price in prices_list
]
# print(prices)

list_of_addresses = soup.find_all("address")
addresses = [
    address.getText().replace("\n", "").strip(" ").replace(" |", "")
    for address in list_of_addresses
]
# print(addresses)

# Selenium part

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for index in range(len(prices)):
    driver.get(FORM_URL)
    time.sleep(2)
    first_question = driver.find_element(
        By.XPATH,
        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div['
        "2]/div/div[1]/div/div[1]/input",
    )
    second_question = driver.find_element(
        By.XPATH,
        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div['
        "2]/div/div[1]/div/div[1]/input",
    )
    third_question = driver.find_element(
        By.XPATH,
        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div['
        "2]/div/div[1]/div/div[1]/input",
    )

    first_question.send_keys(addresses[index])
    second_question.send_keys(prices[index])
    third_question.send_keys(url_list[index])

    driver.find_element(
        By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span'
    ).click()

driver.quit()
