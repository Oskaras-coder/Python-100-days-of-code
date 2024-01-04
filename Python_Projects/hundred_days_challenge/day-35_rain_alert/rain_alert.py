import requests
import os
from twilio.rest import Client

api_key = "5a7f2f99286aeaa08e6873f38f26592c"

account_sid = 'AC49dddace82ae0801568edeb1595e04c8'
auth_token = 'bfe30c095adee072461f232cf776aa6c' 



# https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}

MY_LAT = 54.687157
MY_LONG = 25.279652


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "appid": api_key,

}
# response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
# response.raise_for_status()
# data = response.json()


client = Client(account_sid, auth_token)
message = client.messages \
                .create(
                     body="Lyja tegul lyja.",
                     from_='+17853902915',
                     to='+37069473945'
                 )
print(message.status)
# sending as a alert (twilio.com)