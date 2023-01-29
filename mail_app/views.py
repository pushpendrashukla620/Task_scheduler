from django.shortcuts import render
from django.contrib import messages
from django.conf import settings

# Create your views here.
from django.shortcuts import render
from .models import User
import requests
from django.core.mail import send_mail

# schedule the send_email function to run every hour using django-scheduler
def Register(request):
    if request.method =='POST':
        email=request.POST.get('email')
        try:
            user_obj=User.objects.create(email=email)
            print(user_obj)
            user_obj.save()
            messages.success(request, 'User Registered successfully')
        except Exception as e:
            messages.success(request, 'User Registered successfully')


        
    return render(request,'register.html')
