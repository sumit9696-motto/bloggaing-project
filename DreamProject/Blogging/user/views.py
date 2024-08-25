from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import datetime


# Create your views here.
def home(request):
    cdata = category.objects.all().order_by('-id')[0:12]
    cursor = connection.cursor()
    cursor.execute(
        "select b.*,p.* from user_blogdetail b, user_profile p where b.authorid=p.email order by b.bdate desc limit 0,6")
    bdetail = cursor.fetchall()
    return render(request, 'user/index.html', {"data": cdata, "bdetail": bdetail})


def aboutus(request):
    return render(request, 'user/aboutus.html')


def contactus(request):
    status = False
    if request.method == 'POST':
        Name = request.POST.get("name", "")
        Mobile = request.POST.get("mobile", "")
        Email = request.POST.get("email", "")
        Message = request.POST.get("message", "")
        Address = request.POST.get("address", "")
        res = contact(name=Name, mobile=Mobile, email=Email, message=Message, address=Address)
        res.save()
        status = True

    return render(request, 'user/contactus.html', {'S': status})


def createblogs(request):
    if request.session.get('user'):
        cdata = category.objects.all()
        if request.method == 'POST':
            authorid = request.session.get('user')
            bcategory = request.POST.get('category')
            btopic = request.POST.get('topic')
            bdescription = request.POST.get('description')
            battacment = request.FILES['document']
            bthumbnail = request.FILES['thumbnail']
            res = blogdetail(authorid=authorid, blogcategory=bcategory, topic=btopic, description=bdescription,
                             attachment=battacment, thumbnail=bthumbnail, bdate=datetime.datetime.now())
            res.save()
            return HttpResponse(
                "<script>alert('Your blogs created successfully..');window.location.href='/user/home';</script>")
        return render(request, 'user/createblogs.html', {"category": cdata})
    else:
        return HttpResponse(
            "<script>alert('login first..');window.location.href='/user/signup';</script>")


def latestblogs(request):
    cursor = connection.cursor()
    if (request.GET.get('id') is None):
        cursor.execute(
            "select b.*,p.* from user_blogdetail b, user_profile p where b.authorid=p.email order by b.bdate desc")
    else:
        id = request.GET.get('id')
        cursor.execute(
            "select b.*,p.* from user_blogdetail b, user_profile p where b.authorid=p.email and b.blogcategory='" + id + "' order by b.bdate desc")
    bdetail = cursor.fetchall()
    print(bdetail)
    cdata = category.objects.all().order_by('-id')
    return render(request, 'user/latestblogs.html', {"bdetail": bdetail, "data": cdata})


def myblogs(request):
    if request.session.get('user'):
        return render(request, 'user/myblogs.html')
    else:
        return HttpResponse("<script>alert('Login First..');window.location.href='/user/signin';</script>")


def signup(request):
    status = False
    if request.method == 'POST':
        Name = request.POST.get("sname", "")
        DOB = request.POST.get("dob", "")
        Gender = request.POST.get("gender", "")
        Mobile = request.POST.get("mobile", "")
        Email = request.POST.get("email", "")
        Password = request.POST.get("password", "")
        Profession = request.POST.get("profession", "")
        College = request.POST.get("college", "")
        upic = request.FILES["profile"]
        res = profile(name=Name, dob=DOB, gender=Gender, mobile=Mobile, email=Email, password=Password,
                      profession=Profession, college=College, pic=upic)
        res.save()
        status = True
        return HttpResponse("<script>alert('Now you are registered..');window.location.href='/user/signin';</script>")
    return render(request, 'user/signup.html')


def signin(request):
    if request.method == 'POST':
        uname = request.POST.get('email')
        pwd = request.POST.get('passwd')
        checkuser = profile.objects.filter(email=uname, password=pwd)
        if (checkuser):
            request.session["user"] = uname
            return HttpResponse(
                "<script>alert('Now! you are member of CoderHub..');window.location.href='/user/home';</script>")
        else:
            return HttpResponse(
                "<script>alert('UserId or Password is incorrect..');window.location.href='/user/signin';</script>")
    return render(request, 'user/signin.html')


def logout(request):
    del request.session['user']
    return HttpResponse("<script>alert('Log Out Successfully');window.location.href='/user/home/';</script>")
