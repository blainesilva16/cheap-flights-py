import smtplib, os

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self,cheap_flights):
        try:
            for flight in cheap_flights:
                with smtplib.SMTP(HOST, 587) as connection:
                    connection.starttls()
                    connection.login(user=MY_EMAIL,password=PASSWORD)
                    connection.sendmail(
                        from_addr=MY_EMAIL,
                        to_addrs=MY_EMAIL,
                        msg=f"Subject:We have a cheaper flight for {flight["city"]}!\n\n{flight["info"]}")
        except:
            print("No emails sent because there was no cheaper flight.")
