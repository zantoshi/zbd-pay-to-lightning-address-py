from django.shortcuts import render, redirect
import requests, os


# Create your views here.

def index(request):
    if request.POST:
        # Form Data
        amount = request.POST["amount"] + "000"


        # ZBD API 
        URL = "https://api.zebedee.io/v0/ln-address/send-payment"
        data = { 'lnAddress' : request.POST["lnaddress"], 'amount' : amount, 'comment': 'Sending to a Lightning Address'}
        APIKEY = os.environ.get('APIKEY')
        headers = { "Content-Type":"application/json",  'apikey' : APIKEY }

        # sending get request and saving the response as response object
        r = requests.post(url = URL, json = data , headers = headers )
        # extracting data in json format
        data = r.json()

        print(data)

        if data["success"]:
            return redirect('success')
        else:
            return render(request, 'lightning_address_payment/index.html')

    else:
        return render(request, 'lightning_address_payment/index.html')



def success(request):
    return render(request, 'lightning_address_payment/success.html')
