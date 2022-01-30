from django.shortcuts import render
from os import pipe
from django import http
from django.db import reset_queries
from django.http import response
from django.shortcuts import render, HttpResponse, redirect

# from home.models import Contact
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Event
import json
import datetime

# Create your views here.
def home(request):
    return render(request, "astro/home.html")


def about(request):
    return render(request, "astro/about.html")


def addevent(request):
    if request.method == "POST":
        nm = request.POST.get("Namee")
        disc = request.POST.get("disc")
        urll = ""
        for i in range(1, 100):
            s = "url" + str(i)
            val = request.POST.get(s)
            if val == None:
                break
            elif val != "":
                l = str(val)
                urll += l + "$$"
        info = ""
        for i in range(1, 100):
            s = "info" + str(i)
            val = request.POST.get(s)
            if val == None:
                break
            elif val != "":
                l = str(val)
                info += l + "$$"
        hl = ""
        for i in range(1, 100):
            s = "high" + str(i)
            val = request.POST.get(s)
            if val == None:
                break
            elif val != "":
                l = str(val)
                hl += l + "$$"

        if nm != "" and disc != "":
            event = Event(
                Name=nm, Discription=disc, imgUrls=urll, Info=info, Highlights=hl
            )
            event.save()
        return redirect("addevent")

    else:
        return render(request, "astro/addevents.html")

def showevent(request):
    events = Event.objects.all().order_by('Event_id')
    ev=[]
    for e in events:
        urls = e.imgUrls
        urrr = urls.split('$$')
        

        # info = e.Info
        # inf = info.split('$$')

        # high = e.Highlights
        # hig = high.split('$$')
        
        

        oo = {
            "id":e.Event_id,
            "name":e.Name,
            "disc":e.Discription,
            "img":urrr[0],
            # "urls":urrr,
            # "inf":inf,
            # "hig":hig,
        }
        ev.append(oo)
    evs = {
        "evs":ev
    }


        

    return render(request, 'astro/event.html', evs)
