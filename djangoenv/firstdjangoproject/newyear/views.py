from django.shortcuts import render
from django.http import HttpRequest

import datetime

def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {"newyear": now.month == 1 and now.day == 1})

# Create your views here.
