# ISS-overhead-notifier
 This code sends an email notification if the International Space Station (ISS) is near the user's location and it is currently nighttime. 
 The code performs the following tasks:

    Import necessary libraries: requests, datetime, smtplib, and time.

    Define the user's latitude, longitude, email address, and password as constants.

    Define a function called iss_is_overhead that sends a GET request to the "http://api.open-notify.org/iss-now.json" API to retrieve the current location of the ISS. The function checks if the ISS is within +5 or -5 degrees of the user's position and returns True if it is.

    Define a function called is_night that sends a GET request to the "http://api.sunrise-sunset.org/json" API to retrieve the sunset and sunrise times for the user's location. The function checks if the current time is after sunset or before sunrise and returns True if it is.

    Create a while loop that sleeps for 60 seconds and checks if the ISS is overhead and it is nighttime. If both conditions are met, the code sends an email notification to the user using the SMTP protocol. The print statement in the code logs the time that the notification was sent to the console.

Note: It is important to keep the email address and password secure, and not to share them with others.

