from django.shortcuts import render , redirect

from django.http import HttpResponse
from django.conf import settings
from model1.models import *
import random

from .utils import sent_email_to_user , send_email_with_attachment

def send_email(request):
    # sent_email_to_user() #for common mail
    subject = "This email is from django server with Attachment"
    message = "Hey please find this attach file with this email"
    recipient_list = ["gopalbera6335@gmail.com"]
    file_path = f'{settings.BASE_DIR}/main.xlsx'

    send_email_with_attachment(subject , message , recipient_list , file_path)
    return redirect('/')

def home(request):

    Car.objects.create(car_name = f'nexon-{random.randint(0 , 100)}')

    people=[
        {"name":"Amit Shah","age":65},
        {"name":"Arvind Kejarival ","age":-50},
        {"name":"Nitin Gadkari ","age":63},
        {"name":"Rahul Gandhi","age":15},
        {"name":"Yogi Aadityanath","age":49}
    ]
    
    return render(request,"home/index.html",context={"people" : people})

def contact(request):
    return render(request,"home/contact.html")


def about(request):
    return render(request,"home/about.html")

def success_page(request):
    return HttpResponse("<h1>Hey, This is a Success page </h1>")