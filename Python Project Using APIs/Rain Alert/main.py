# Note! For the code to work you need to replace all the placeholders with
# Your own details. e.g. account_sid, lat/lon, from/to phone numbers.

import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
# api_key = os.environ.get("edea0b121392d2a81cc491a3821ac50a")
api_key = "edea0b121392d2a81cc491a3821ac50a"
account_sid = "ACc36296814fad27a4deaab9899530dcb6"
# auth_token = os.environ.get("7d81f9ef1a2b2a28d833ea4f10774714")
auth_token = "7d81f9ef1a2b2a28d833ea4f10774714"


weather_params = {
    "lat": "23.014509",
    "lon": "72.591759",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    # , http_client = proxy_client

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+14044713439",
        to="+918320210032"
    )
    print(message.status)
