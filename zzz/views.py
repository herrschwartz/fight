from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import models
from .models import Fighters
from django.db.models import Q
import json

# Create your views here.

def index(request):
    data = {}
    data['orderid'] = 24
    return render(request,"main.html", data)

def searchName(request):
    if request.method == 'POST':
        print(request.body)
        print(request.POST)
        j = json.loads(request.body)
        p = j['search']

        data = {}
        for n in p.split():
            f = Fighters.objects.filter(Q(first_name__icontains=n) | Q(last_name__icontains=n))
        fighterName = []
        for i in f:
            fighterName.append(i.first_name + " " + i.last_name)

        data['name'] = fighterName
        return JsonResponse(data)
    else:
        p = request.POST.get('data')
        print(p)
        return JsonResponse({"data": p})
