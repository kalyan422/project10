from django.shortcuts import render
from django.views import View
import requests
import random
from django.core.mail import send_mail
from django.http import HttpResponse
from project10.settings import EMAIL_HOST_USER
from .forms import RegForm
# Create your views here.
class Home(View):
    def get(self,request):
        rf=RegForm()
        con_dic={'rf':rf}
        return render(request,'home.html',context=con_dic)
class Reg(View):
    def post(self,request):
        otp=str(random.randint(10000000,99999999))
        print(otp)
        mobno=request.POST["MobileNo"]
        emailid=request.POST["Emailid"]
        resp=requests.post('https://textbelt.com/text',{
            'phone':mobno,
            'message':otp,
            'key':'deb651692eabe6a8c4dc2bf4c540d840302c14beufATt5cvEXUzaN5EDcNM17s9q',
        })
        print(resp.json())
        send_mail("otp for registration ",otp,EMAIL_HOST_USER,[emailid],fail_silently=True)
        return HttpResponse("otp send to mobileno and email")
