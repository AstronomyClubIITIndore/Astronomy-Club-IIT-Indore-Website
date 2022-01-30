from venv import EnvBuilder
from wsgiref.util import request_uri
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
from .models import Event, Blog
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

def eventDetail(request, eid):
    event = Event.objects.filter(Event_id=eid).first()
    urls = event.imgUrls
    urrr = urls.split('$$')
    urrr.pop()
        

    info = event.Info
    inf = info.split('$$')
    inf.pop()


    high = event.Highlights
    hig = high.split('$$')
    hig.pop()





    return render(request, 'astro/event_detail.html',{"Name":event.Name, "Disc":event.Discription,"imgs":urrr, "infs":inf, "higs":hig})

def addblog(request):
    if request.method == "POST":
        T = request.POST.get("title")
        D = request.POST.get("disc")
        C = request.POST.get("content")
        hi = request.POST.get("headimage")
        blog = Blog(Title=T, headimg=hi, Discription=D,Content=C)
        if T !="" and D !="" and C !="" and hi !="":
            blog.save()
            print("Save")

    return render(request, 'astro/AddBlog.html')

def blogs(request):

    blogs = Blog.objects.all().order_by('Blog_id')
    send =[]
    for b in blogs:
        oo ={
            "Title":b.Title,
            "id":b.Blog_id,
            "disc":b.Discription,
            "img":b.headimg
        }
        send.append(oo)

    

    return render(request, 'astro/blogs.html', {"bls":send})
def readblog(request, bid):
    b = Blog.objects.filter(Blog_id=bid).first()
    oo ={
            "Title":b.Title,
            "id":b.Blog_id,
            "disc":b.Discription,
            "img":b.headimg,
            "cnt":b.Content,
        }

    return render(request,'astro/Blog_detail.html',oo)



