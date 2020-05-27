from django.shortcuts import render
import requests
from django.http import JsonResponse
import json
import datetime as DT
from .models import Valute

def index(request):
    return render(request, 'main/index.html')


def get_value(request):
    if request.method=='GET':
        url='https://www.cbr-xml-daily.ru/daily_json.js'
        response=requests.get(url)
        data={}
        data.update({'Date': response.json().get('Date')})
        data.update({'USD': response.json().get('Valute').get('USD').get('Value')})
        data.update({'EUR': response.json().get('Valute').get('EUR').get('Value')})
        valute=Valute()
        valute.USD=response.json().get('Valute').get('USD').get('Value')
        valute.EUR=response.json().get('Valute').get('EUR').get('Value')
        data_date=response.json().get('Date')
        valute.date=DT.datetime.strptime(data_date[:data_date.index('+')], '%Y-%m-%dT%H:%M:%S')
        valute.save()
        return JsonResponse(data)
