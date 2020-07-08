from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import requests
import json
from newapp.models import boot
from rest_framework.response import Response
from rest_framework.views import APIView
from newapp.serializers import bootSerializer
from django.contrib.auth import authenticate
from django import forms
from django.urls import reverse

from django.contrib.auth.forms import AuthenticationForm



# Create your views here.
def login(request):
    return render(request, 'signup.html')
def signin(request):
    return render(request, 'signin.html')

def submitUser(request):
    Name = request.GET['name']
    Email = request.GET['Email']
    Password = request.GET['Password']
  

    url = "http://127.0.0.1:8000/boot/"

    payload = {"Name": Name, "Email":Email, "Password":Password}
    payload = json.dumps(payload)
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    data = response.text

    return render(request, 'temp.html')

def submitUserIn(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('Password')
        email=request.POST.get('Email')
        print(username,password)
        user = authenticate(username=username, password=password, email=email)
        print(user)
        if not user:
             return render(request, 'temp.html', {})
                
                
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    
    
    # payload = {"Name": Name, "Email":Email, "Password":Password}
    
    # headers = {
    # 'Content-Type': 'application/json'
    # }
    
    # response = requests.request("GET", url, headers=headers, data = payload)
    # print(response.text)
    

   
    #return
    # def clean(self,*args,**kwargs):
    #     Name=self.cleaned_data.get('name')
    #     Password=self.cleaned_data.get('Password')
    #     print(Name)
    #     print(Password)

    
    


    

    









    

   