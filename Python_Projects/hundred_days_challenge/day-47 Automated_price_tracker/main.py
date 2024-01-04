import smtplib
from pprint import pprint

import requests
from bs4 import BeautifulSoup
import lxml

my_email = "pyt.test.32@gmail.com"
password = "Testestest12343212"

# rwxjlyzchbykbnaf  - App- password for this computer
URL_PRESSURE_COOKER = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 "
    "Safari/537.36",
    "Accept-Language": "lt-LT,lt;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,pl;q=0.5",
}
response = requests.get(URL_PRESSURE_COOKER, headers=header)
soup = BeautifulSoup(response.text, "lxml")

whole_number = soup.find(name="span", class_="a-price-whole").getText()
fraction_number = soup.find(name="span", class_="a-price-fraction").getText()
price = float(whole_number + fraction_number)
print(price)


if price < 100:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="osafinas@gmail.com",
            msg=f"Subject:Notification about low price!!\n\n The product is below your asking price - ${price}, buy now!",
        )
