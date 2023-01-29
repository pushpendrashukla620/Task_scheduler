# send_mail

This project sends delhi weather data to it's registered users automatically after every hour.

Just add your email and password in settings.py

Start the server and register your mail to get weather update every hour(For registering you mail to get weather updates go to->  http://127.0.0.1:8000/  and register your mail ).

This project uses django scheduler to send mail to it's registered users every hour. We can also change task which it do i have used it for sending mail.

It is recommended to use this command for stating the server -> python manage.py runserver --noreload
