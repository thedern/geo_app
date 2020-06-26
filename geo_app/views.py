"""
# Uncomment to create your function-based views here.
from django.shortcuts import render
import requests

def home(request):
    url = 'http://api.ipstack.com/{}?access_key=b49fc28743af67723f7f03174fca0f52'
    ip = '108.4.16.142'
    geodata = requests.get(url.format(ip)).json()

    # create a dictionary of a subset of the data returned from the API
    ip_data = {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    }

    # create variable, we just named it 'context' which contains
    context = {'data': ip_data}
    return render(request, 'home.html', context)

    # or just send the geodata directly
    # return render(request, 'home.html', geodata)
"""

# if using class-based views instead of function-based views, use this code below
from django.views import View
from django.shortcuts import render
import requests


class HomeView(View):

    def get(self, request):
        url = 'http://api.ipstack.com/{}?access_key={}'
        key = 'b49fc28743af67723f7f03174fca0f52'
        ip = '108.4.16.142'
        geodata = requests.get(url.format(ip, key)).json()
        return render(request, 'home.html', context=geodata)
