import requests
from requests.auth import HTTPBasicAuth
import json

paybill_number = ''

def get_token():
  '''
  generates the access_token
  '''
  consumer_key = "0qMmNRAVPqBGpK1bOTsZGLM2lnsNBvW3"
  consumer_secret = "OMV1rQNUU2ViaCco"
  api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
  
  r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
  response = json.loads(r.text)
  return response['access_token']
  
def customer_to_business(phone_number=''):
  access_token = get_token()
  api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
  headers = {"Authorization": "Bearer %s" % access_token}
  request = { "ShortCode":"600477",
  "CommandID":"CustomerPayBillOnline",
  "Amount":" ",
  "Msisdn":phone_number,
  "BillRefNumber":" " }

  response = requests.post(api_url, json = request, headers=headers)
  print (response.text)
  

def business_to_customer(phone_number=''):
  access_token = get_token()
  api_url = "https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest"
  headers = { "Authorization": "Bearer %s" % access_token }
  request = {
    "InitiatorName": " ",
    "SecurityCredential":" ",
    "CommandID": " ",
    "Amount": " ",
    "PartyA": paybill_number,
    "PartyB": phone_number,
    "Remarks": " ",
    "QueueTimeOutURL": "http://your_timeout_url",
    "ResultURL": "http://your_result_url",
    "Occasion": " "
  }
  
  response = requests.post(api_url, json = request, headers=headers)
  print (response.text)