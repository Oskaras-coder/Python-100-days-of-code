from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

SPEED_TEST_URL = "https://www.speedtest.net/"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        driver.get(SPEED_TEST_URL)
        driver.find_element(By.CLASS_NAME, value="start-text").click()
        time.sleep(60)
        self.down = driver.find_element(By.XPATH,
                                        value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                              '3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = driver.find_element(By.XPATH,
                                      value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                            '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
                                            '2]/div/div[2]/span').text

        print(self.down)
        print(self.up)

    def tweet_at_provider(self):  # got info don't want to send anything yet
        driver.get("https://twitter.com/login")

        time.sleep(2)
        email = driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div['
                                                    '1]/form/div/div[1]/label/div/div[2]/div/input')
        password = driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div['
                                                       '1]/form/div/div[2]/label/div/div[2]/div/input')

        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(5)
        tweet_compose = driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div['
                                                            '2]/main/div/div/div/div/div/div[2]/div/div[2]/div['
                                                            '1]/div/div/div/div['
                                                            '2]/div[1]/div/div/div/div/div/div/div/div/div/div['
                                                            '1]/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)

        time.sleep(2)
        driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
