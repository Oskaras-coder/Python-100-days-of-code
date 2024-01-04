from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")
#
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
#
# print(f"The price is {price_dollar}.{price_cents}")

driver.get("https://www.python.org/")
search_bar = driver.find_element(By.NAME, value="q").tag_name
button = driver.find_element(By.ID, value="submit").size
print(search_bar)
print(button)

documentation = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation.text)


link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[1]/a')
print(link.text)


# driver.close()  # Closes tab
driver.quit()  # Quit entire program
