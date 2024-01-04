from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://tinder.com/")

driver.find_element(By.LINK_TEXT, value="Log in").click()
time.sleep(3)
driver.find_element(By.XPATH, value='//*[@id="q-1240333203"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div['
                                    '2]/button/div[2]/div[2]/div/div').click()

time.sleep(3)

username = ""
password = ""

fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window) # switch to a pop-up window

# driver.find_element(By.XPATH, value='//*[@id="u_0_g_Vq"]').click()

time.sleep(3)

driver.find_element(By.ID, value="email").send_keys(username)
driver.find_element(By.ID, value="pass").send_keys(password)
driver.find_element(By.XPATH, value='//*[@id="u_0_0_Uh"]').click()

# driver.find_element()
# for i in range(10):
#     driver.find_element(By.XPATH, value='//*[@id="q488047873"]/div/div[1]/div/div/main/div/div/div[1]/div/div['
#                                         '3]/div/div[2]/button/span/span/svg/path')
