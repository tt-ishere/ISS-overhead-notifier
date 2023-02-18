import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 5.603717  # your latitude
MY_LNG = -0.186964  # your longitude
MY_EMAIL = "youremail@gmail.com"
PASSWORD = "your_password"


# get iss location
def iss_is_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    # your position is within +5 0r -5 degrees of iss position
    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (
        MY_LNG - 5 <= iss_longitude <= MY_LNG + 5
    ):
        return True


# is it night?
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get("http://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if iss_is_overhead() and is_night():
        # send mail
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject: ISS location\n\nLOOK UP",
            )
            print(f"Notification sent at {datetime.hour}:{datetime.minute}")
