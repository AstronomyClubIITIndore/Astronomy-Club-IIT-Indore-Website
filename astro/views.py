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
from django.contrib.auth import authenticate,  login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
import json
import datetime

# Create your views here.
def home(request):
    return render(request, 'astro/home.html')

def about(request):
    return render(request, 'astro/about.html')

def addevent(request):
    if request.method == "POST":
        print("Fff")
        print("Fff")
        return redirect('addevent')
    else:
        print("Fffjnono")
        return render(request, 'astro/addevents.html')
