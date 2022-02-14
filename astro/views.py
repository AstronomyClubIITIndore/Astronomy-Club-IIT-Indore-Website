from audioop import lin2adpcm
from code import interact
from hashlib import new
from turtle import title
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
from .decorators import unauthenticated_user, allowed_users

from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Event, Blog, Profile, Publication, Interview, Photo
import json
import datetime

# Create your views here.
def home(request):
    p = Interview.objects.all().order_by('interview_id').first()
    oo ={
            "Title":p.Title,
            "Interviewee":p.Interviewee,
            "Disc":p.Disc,
            "Thumbnail":p.Thumbnail,
            "Video":p.Video,

        }
    e = Event.objects.all().order_by('Event_id').first()
    urls = e.imgUrls
    urrr = urls.split('$$')
        

        # info = e.Info
        # inf = info.split('$$')

        # high = e.Highlights
        # hig = high.split('$$')
        
        

    ooo = {
            "id":e.Event_id,
            "name":e.Name,
            "disc":e.Discription,
            "img":urrr[0],
            # "urls":urrr,
            # "inf":inf,
            # "hig":hig,
        }


    return render(request, "astro/home.html", {"p":oo, "e":ooo })


def about(request):
    return render(request, "astro/about.html")


@allowed_users(allowed_roles=["developers", "Admins"])
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
    events = Event.objects.all().order_by("Event_id")
    ev = []
    for e in events:
        urls = e.imgUrls
        urrr = urls.split("$$")

        # info = e.Info
        # inf = info.split('$$')

        # high = e.Highlights
        # hig = high.split('$$')

        oo = {
            "id": e.Event_id,
            "name": e.Name,
            "disc": e.Discription,
            "img": urrr[0],
            # "urls":urrr,
            # "inf":inf,
            # "hig":hig,
        }
        ev.append(oo)
    evs = {"evs": ev}

    return render(request, "astro/event.html", evs)


def eventDetail(request, eid):
    event = Event.objects.filter(Event_id=eid).first()
    urls = event.imgUrls
    urrr = urls.split("$$")
    urrr.pop()

    info = event.Info
    inf = info.split("$$")
    inf.pop()

    high = event.Highlights
    hig = high.split("$$")
    hig.pop()

    return render(
        request,
        "astro/event_detail.html",
        {
            "Name": event.Name,
            "Disc": event.Discription,
            "imgs": urrr,
            "infs": inf,
            "higs": hig,
        },
    )


@allowed_users(allowed_roles=["developers", "Admins"])
def addblog(request):
    if request.method == "POST":
        T = request.POST.get("title")
        D = request.POST.get("disc")
        C = request.POST.get("content")
        hi = request.POST.get("headimage")
        auth = request.POST.get("author")
        dt = request.POST.get("date")
        blog = Blog(Title=T, headimg=hi, Discription=D, Content=C, Author=auth, Date=dt)
        if T != "" and D != "" and C != "" and hi != "":
            blog.save()

    return render(request, "astro/AddBlog.html")


def blogs(request):

    blogs = Blog.objects.all().order_by("Blog_id")
    send = []
    for b in blogs:
        oo = {
            "Title": b.Title,
            "id": b.Blog_id,
            "disc": b.Discription,
            "img": b.headimg,
            "aut": b.Author,
            "dt": b.Date,
        }
        send.append(oo)

    return render(request, "astro/blogs.html", {"bls": send})


def readblog(request, bid):
    b = Blog.objects.filter(Blog_id=bid).first()
    oo = {
        "Title": b.Title,
        "id": b.Blog_id,
        "disc": b.Discription,
        "img": b.headimg,
        "cnt": b.Content,
        "aut": b.Author,
        "dt": b.Date,
    }

    return render(request, "astro/Blog_detail.html", oo)


@allowed_users(allowed_roles=["developers", "Admins"])
def addmember(request):
    if request.method == "POST":
        nm = request.POST.get("Name")
        abt = request.POST.get("abt")
        branchyear = request.POST.get("branchyear")
        mno = request.POST.get("mno")
        email = request.POST.get("email")
        por = request.POST.get("POR")
        img = request.POST.get("img")
        old = request.POST.get("old")
        new = request.POST.get("new")
        ghub = request.POST.get("ghub")
        lin = request.POST.get("lin")
        insta = request.POST.get("insta")
        fb = request.POST.get("fb")
        act = ""
        for i in range(1, 100):
            s = "url" + str(i)
            s1 = "urll" + str(i)
            head = request.POST.get(s)
            dc = request.POST.get(s1)
            if head == None or dc == None:
                break
            elif head != None and dc != None:
                l = str(head)
                j = str(dc)
                act += l + "##" + j + "$$"

        intrests = ""
        for i in range(1, 100):
            s = "info" + str(i)
            val = request.POST.get(s)
            if val == None:
                break
            elif val != "":
                l = str(val)
                intrests += l + "$$"

        print(nm, abt, branchyear, mno, email, por, img, old, new, act, intrests)
        b = branchyear + "$$" + mno + "$$" + email + "$$" + por
        lll = str(ghub) + "$$" + str(lin) + "$$" + str(insta) + "$$" + str(fb)

        ol = ""
        if old == 1:
            ol = "old"
        elif new == 1:
            ol = "new"

        profile = Profile(
            Name=nm,
            branch_year_mobilenumber_email_por=b,
            About=abt,
            Intrests=intrests,
            Activities=act,
            img=img,
            git_lin_insta_fb=lll,
            old=ol,
        )
        if (
            nm != ""
            and b != ""
            and abt != ""
            and intrests != ""
            and act != ""
            and img != ""
            and lll != ""
        ):
            profile.save()
    return render(request, "astro/addMember.html")


def team(request):
    members = Profile.objects.all().order_by("memb_id")
    olds = []
    news = []

    for b in members:
        data = b.branch_year_mobilenumber_email_por
        dat = data.split("$$")

        if b.old == "a":

            oo = {
                "Name": b.Name,
                "id": b.memb_id,
                "img": b.img,
                "branch_year": dat[0],
                "mno": dat[1],
                "email": dat[2],
                "por": dat[3],
                "abt": b.About,
            }
            olds.append(oo)
        else:
            oo = {
                "Name": b.Name,
                "id": b.memb_id,
                "img": b.img,
                "branch_year": dat[0],
                "mno": dat[1],
                "email": dat[2],
                "por": dat[3],
                "abt": b.About,
            }
            news.append(oo)

    return render(request, "astro/team.html", {"olds": olds, "news": news})


def profile(request, mid):
    b = Profile.objects.filter(memb_id=mid).first()
    data = b.branch_year_mobilenumber_email_por
    dat = data.split("$$")

    ints = b.Intrests
    int = ints.split("$$")
    int.pop()

    actvs = (b.Activities,)
    acts = actvs[0].split("$$")
    acs = acts.pop()

    handles = (b.git_lin_insta_fb,)
    hands = handles[0].split("$$")
    print(hands)

    activities = []
    for ac in acts:
        d = ac.split("##")
        o = {
            "Heading": d[0],
            "Disc": d[1],
        }

        activities.append(o)

    main = {
        "Name": b.Name,
        "id": b.memb_id,
        "img": b.img,
        "branch_year": dat[0],
        "mno": dat[1],
        "email": dat[2],
        "por": dat[3],
        "abt": b.About,
        "ints": int,
        "git": hands[0],
        "linkdIn": hands[1],
        "insta": hands[2],
        "fb": hands[3],
    }

    # old new wala dekh lena

    return render(
        request, "astro/member_profile.html", {"p": main, "aa": activities, "int": int}
    )


def Publications(request):
    pubs = Publication.objects.all().order_by("publication_id")
    pus = []
    for p in pubs:
        oo = {
            "publication_id": p.publication_id,
            "Thumbnail_link": p.Thumbnail_link,
            "Name": p.Name,
            "About": p.About,
            "Link": p.Link,
        }
        pus.append(oo)

    return render(request, "astro/publications.html", {"pp": pus})


@allowed_users(allowed_roles=["developers", "Admins"])
def addpublications(request):
    if request.method == "POST":
        nm = request.POST.get("Name")
        abt = request.POST.get("About")
        tmbnl = request.POST.get("Thumbnail")
        file_link = request.POST.get("Link")
        pub = Publication(Name=nm, About=abt, Thumbnail_link=tmbnl, Link=file_link)
        if nm != "" and abt != "" and tmbnl != "" and file_link != "":
            pub.save()

    return render(request, "astro/addpublications.html")


@allowed_users(allowed_roles=["developers", "Admins"])
def addinterview(request):
    if request.method == "POST":
        Title = request.POST.get("Title")
        Interviewee = request.POST.get("Interviewee")
        Disc = request.POST.get("Disc")
        Video = request.POST.get("Video")
        Thumbnail = request.POST.get("Thumbnail")
        int = Interview(
            Title=Title,
            Thumbnail=Thumbnail,
            Interviewee=Interviewee,
            Disc=Disc,
            Video=Video,
        )
        if (
            Title != ""
            and Interviewee != ""
            and Thumbnail != ""
            and Disc != ""
            and Video != ""
        ):
            int.save()

    return render(request, "astro/addinterview.html")


def interview(request):
    pubs = Interview.objects.all().order_by("interview_id")
    pus = []
    for p in pubs:
        oo = {
            "Title": p.Title,
            "Interviewee": p.Interviewee,
            "Disc": p.Disc,
            "Thumbnail": p.Thumbnail,
            "Video": p.Video,
        }
        pus.append(oo)

    return render(request, "astro/Interview.html", {"pp": pus})


# @allowed_users(allowed_roles=[ 'developers','Admins'])
def addimage(request):
    if request.method == "POST":
        grp = request.POST.get("grp")
        link = request.POST.get("link")

        int = Photo(Group=grp, Link=link)
        if grp != "" and link != "":
            int.save()

    return render(request, "astro/addimage.html")


def gallery(request):
    pubs = Photo.objects.all().order_by("Photo_id")
    arts = []
    clks = []
    for p in pubs:
        if p.Group == "art":
            # arts.append(p.Link)
            oo = {
                "li": p.Link,
                "id": p.Photo_id,
            }
            arts.append(oo)
        else:
            oo = {
                "li": p.Link,
                "id": p.Photo_id,
            }
            clks.append(oo)
            # clks.append(p.Link)

    return render(request, "astro/gallery.html", {"arts": arts, "clks": clks})


@allowed_users(allowed_roles=["Admins"])
def workspace(request):
    if request.method == "POST":
        nm = request.POST.get("uName")
        email = request.POST.get("email")
        name = request.POST.get("name")
        p1 = request.POST.get("p1")
        p2 = request.POST.get("p2")
        print(nm, email, name)
        myuser = User.objects.create_user(nm, email, p1)
        myuser.first_name = name
        # print(myuser)
        myuser.save()
        group = Group.objects.get(name="developers")
        myuser.groups.add(group)

    userl = []
    group = Group.objects.get(name="developers")
    users = list(group.user_set.all())
    for user in users:
        oo = {
            "Name": user.first_name,
            "username": user,
        }
        userl.append(oo)

    return render(request, "astro/workspace.html", {"uu": userl})


def loginall(request):
    if request.method == "POST":
        nm = request.POST.get("uName")
        p2 = request.POST.get("p2")
        user = authenticate(username=nm, password=p2)
        if user is not None:
            login(request, user)
            if user.groups.filter(name="Admins").exists():
                return redirect("workspace")

            else:
                return redirect("home")
        else:
            print("kk")
            return redirect("home")

    return render(request, "astro/login.html")


def logoutall(req):
    logout(req)
    return redirect("home")


# Delete section#3333333333333333333333333333333333333333333333333333333333333333333333333


@allowed_users(allowed_roles=["developers", "Admins"])
def deleve(request, eid):
    post = Event.objects.filter(Event_id=eid).first()
    post.delete()
    return redirect("showevent")


@allowed_users(allowed_roles=["developers", "Admins"])
def delblog(request, bid):
    post = Blog.objects.filter(Blog_id=bid).first()
    post.delete()

    return redirect("blogs")


@allowed_users(allowed_roles=["developers", "Admins"])
def delprof(request, pid):
    post = Profile.objects.filter(memb_id=pid).first()
    post.delete()
    return redirect("team")


@allowed_users(allowed_roles=["developers", "Admins"])
def delpub(request, puid):
    post = Publication.objects.filter(publication_id=puid).first()
    post.delete()
    return redirect("addpublications")


@allowed_users(allowed_roles=["Admins"])
def delmember(request, mid):
    m = User.objects.get(username=mid)
    m.delete()

    return redirect("workspace")


@allowed_users(allowed_roles=["developers", "Admins"])
def delphoto(request, Photo_id):
    m = Photo.objects.get(Photo_id=Photo_id)
    m.delete()

    return redirect("gallery")
