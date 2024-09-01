from django.shortcuts import render, HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
# return HttpResponse("This is a about page")
# Create your views here.

def contact(request):
    if request.method == 'POST':
        mail = request.POST.get("mail")
        password = request.POST.get("password")
        contact = Contact(mail=mail,password=password,date=datetime.today())
        contact.save()
        messages.success(request, "Your response has been recorded!")
    return render(request,'contact.html')

# return HttpResponse("This is a contact page")
# def services(request):
# return render(request,'services.html')
# return HttpResponse("This is a service page")

def policy(request):
    return render(request,'policy.html')
