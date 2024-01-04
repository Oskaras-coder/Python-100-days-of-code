import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

yesterday = datetime.now().date() - timedelta(days=1)
load_dotenv()

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": os.getenv('STOCK_API'),
}

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.
#  e.g. [new_value for (key, value) in dictionary.items()]
response = requests.get("https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
all_stock_data = response.json()
print(all_stock_data)
yesterdays_stock_price = float(all_stock_data["Time Series (Daily)"][f"{yesterday}"]["4. close"])

# TODO 2. - Get the day before yesterday's closing stock price
two_days_ago_stock_price = float(all_stock_data["Time Series (Daily)"][f"{yesterday - timedelta(days=1)}"]["4. close"])

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
#  Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(float(yesterdays_stock_price) - float(two_days_ago_stock_price))

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day
#  before yesterday.
percentage_difference = abs(100 - (yesterdays_stock_price * 100 / two_days_ago_stock_price))

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage_difference > 5:
    print("Get news!")
## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint:
#  https://stackoverflow.com/questions/509211/understanding-slice-notation


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
