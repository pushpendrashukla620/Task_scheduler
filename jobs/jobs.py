import datetime
from django.conf import settings
from mail_app.models import User
import requests
from django.core.mail import send_mail

def get_weather():
    response = requests.get('https://api.open-meteo.com/v1/forecast?latitude=28.65&longitude=77.23&current_weather=true')
    weather_data = response.json()
    return weather_data

def send_fmail():
    weather_data = get_weather()
    subject = "Weather Update for Delhi"
    message = f"The current temperature in Delhi is {weather_data['current_weather']['temperature']} degrees."
    print(message)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email for user in User.objects.all()]
    send_mail(subject, message, email_from, recipient_list)


def schedule_api():
    send_fmail()