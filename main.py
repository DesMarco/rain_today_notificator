import smtplib
import requests

password = "HERE_YOUR_GOOGLE_APP_PASSWORD"
email_from = "YOUR_EMAIL"
email_to = "DESTINATION_EMAIL"
LAT = 39.511193 #WRITE YOUR LATITUDE HERE
LONG = -0.456659 #WRITE YOUR LONGITUDE HERE
api_key = "PUT YOUR openweathermap.org/ API KEY HERE"
url = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat" : LAT,
    "lon" : LONG,
    "appid" : api_key,
    "cnt" : 4,
 }

response = requests.get(url, params=parameters)
response.raise_for_status()
weather_data = response.json()
print(weather_data)

forecasts = range(4)
twelve_hours_rain_check =  []

def check_clouds():
    for n in forecasts:
        three_first_hours_check = weather_data["list"][n]
        three_first_hours_check = three_first_hours_check["weather"][0]
        three_first_hours_check = three_first_hours_check["id"]
        twelve_hours_rain_check.append(three_first_hours_check)

def send_email():
    umbrella = False
    for code in twelve_hours_rain_check:
        if code < 700:
            umbrella = True
    if umbrella:
        print("Pick an umbrella!")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email_from, password=password)
            connection.sendmail(
                from_addr=email_from,
                to_addrs=email_to,
                msg="Subject: RAINING TODAY\n\nPick an umbrella, today it will rain!"
            )

check_clouds()
send_email()
