from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

number = driver.find_element(By.ID, value="articlecount")  # Same
article = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(article.text)
# article.click()

# print(number.text.split(" a")[0])

portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# portals.click()

search_click = driver.find_element(By.LINK_TEXT, value="Search")
search_click.click()

search = driver.find_element(By.NAME, value="search")
search.send_keys("python")
search.send_keys(Keys.ENTER)
# driver.quit()
