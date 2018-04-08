from django.shortcuts import render
from django.http import HttpResponse
from payments.models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import requests
import urllib.request,urllib.parse
import json
from .models import Payment


def send_money(request):

    template = 'index.html'

    if request.method == 'POST':
        #getting values from post
        
        phone_number = request.POST.get('phone_number')
        amount = request.POST.get('amount')

        #adding the values in a context variable 
        context = {            
            'phone_number': phone_number,
            'amount': amount,
            'message': 'Saved successfully'
        }

        payment = Payment.objects.create(
            user=request.user,
            amount=amount,
            phone_number=phone_number
        )  

        payment.save()

        if payment.id:
            return render(request, template, context)
    
        return render(request, template, {'error': 'Not saved'})
    else:
        # if post request is not true 
        #returing the form template 
        
        return render(request, template)


def request_url(request):
  '''
  The end-point that receives the response of the transaction
  '''
  response = request.POST.get("response")
  print (response)

def queue_timeout_response(request):
  '''
  The timeout end-point that receives a timeout response.
  '''
  response = request.POST.get("response")
  print (response)


# def user(request):
#     user = User.objects.all()
#     context = {
#         'user':user
#     }
#    return render(request,'index.html',context)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
   