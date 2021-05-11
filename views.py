from django.shortcuts import render
import datetime
# Create your views here.

def login(request,email,password):
    date=datetime.datetime.now()
    return render(request,'login.html',{'email':email, 'pass':password, 'dt':date, 'sname':'raja',
     'sroll':'py123', 'sbranch':'django', 'saddress':'bangalore'})

