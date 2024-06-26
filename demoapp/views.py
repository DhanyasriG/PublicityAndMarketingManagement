from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import CustomerRegistrationForm, NewspaperForm, PompletForm, HorrorForm, ActionForm, DevotionalForm, \
    InstaForm
from .models import Customer, Admin


def index(request):
    return render(request,"index.html")

def registration(request):
    form = CustomerRegistrationForm()
    if request.method == "POST":
        formdata = CustomerRegistrationForm(request.POST)
        if formdata.is_valid():
            formdata.save()
            msg="You Registered Successfully"
            return render(request, "login.html", {"cusform": form,"msg":msg})
        else:
            msg = "Failed to Register "
            return render(request, "registration.html", {"cusform": form, "msg": msg})
    return render(request,"registration.html",{"cusform":form})


def newspaper(request):
    form=NewspaperForm()
    if request.method == "POST":
        formdata = NewspaperForm(request.POST,request.FILES)
        if formdata.is_valid():
            formdata.save()
            msg = "added Successfully"
            return render(request, "newspaper.html", {"newsform": form, "msg": msg})
        else:
            msg = "Failed to add "
            return render(request, "newspaper.html", {"newsform": form, "msg": msg})
    return render(request, "newspaper.html", {"newsform": form})

def pomplet(request):
    form=PompletForm()
    if request.method == "POST":
        formdata = PompletForm (request.POST,request.FILES)
        if formdata.is_valid():
            formdata.save()
            msg = "added Successfully"
            return render(request, "pamphalet.html", {"pomform": form, "msg": msg})
        else:
            msg = "Failed to add "
            return render(request, "pamphalet.html", {"pomform": form, "msg": msg})
    return render(request, "pamphalet.html", {"pomform": form})

def writer(request):
    return render(request,"writer.html")

def login(request):
    return render(request,"login.html")

def checklogin(request):
    uname = request.POST["eusername"]
    pwd = request.POST["epassword"]

    flag = Customer.objects.filter(Q(username=uname) & Q(password=pwd))

    print(flag)

    if flag:
        emp = Customer.objects.get(username=uname)
        print(emp)
        request.session["eid"] = emp.id
        request.session["ename"] = emp.fullname
        return render(request, "login.html", {"eid": emp.id, "ename": emp.fullname})
    else:
        msg = "Login Failed"
        return render(request, "index.html", {"msg": msg})

def horror(request):
    form = HorrorForm()
    if request.method == "POST":
        formdata = HorrorForm(request.POST)
        if formdata.is_valid():
            formdata.save()
            msg = "added Successfully"
            return render(request, "horror.html", {"horform": form, "msg": msg})
        else:
            msg = "Failed to Register "
            return render(request, "horror.html", {"horform": form, "msg": msg})
    return render(request, "horror.html", {"horform": form})

def action(request):
    form = ActionForm()
    if request.method == "POST":
        formdata = ActionForm(request.POST)
        if formdata.is_valid():
            formdata.save()
            msg = "added Successfully"
            return render(request, "action.html", {"actform": form, "msg": msg})
        else:
            msg = "Failed to Register "
            return render(request, "action.html", {"actform": form, "msg": msg})
    return render(request, "action.html", {"actform": form})

def devotional(request):
    form = DevotionalForm()
    if request.method == "POST":
        formdata = DevotionalForm(request.POST)
        if formdata.is_valid():
            formdata.save()
            msg = "added Successfully"
            return render(request, "devotional.html", {"devform": form, "msg": msg})
        else:
            msg = "Failed to Register "
            return render(request, "devotional.html", {"devform": form, "msg": msg})
    return render(request, "devotional.html", {"devform": form})

def instagram(request):
    form = InstaForm()
    if request.method == "POST":
        formdata = InstaForm(request.POST)
        if formdata.is_valid():
            formdata.save()
            msg = "added Successfully"
            return render(request, "instagram.html", {"insform": form, "msg": msg})
        else:
            msg = "Failed to send "
            return render(request, "instagram.html", {"insform": form, "msg": msg})
    return render(request, "instagram.html", {"insform": form})


def adminlogin(request):
    return render(request,"adminlogin.html")

def checkadminlogin(request):
    uname = request.POST["ausername"]
    pwd = request.POST["apassword"]

    flag = Admin.objects.filter(Q(username__exact=uname) & Q(password__exact=pwd))
    print(flag)

    if flag:
        admin = Admin.objects.get(username=uname)
        print(admin)
        request.session["auname"] = admin.username
        return render(request, "adminhome.html", {"auname": admin.username})
    else:
        msg = "Login Failed"
        return render(request, "adminlogin.html", {"msg": msg})


def adminhome(request):
    auname=request.session["auname"]
    return render(request,"adminhome.html",{"auname":auname})

def viewcustomers(request):
    auname=request.session["auname"]
    cuslist = Customer.objects.all()
    count = Customer.objects.count()
    return render(request,"viewcustomer.html",{"auname":auname,"cuslist":cuslist,"count":count})

def adminlogout(request):
    return render(request,"adminlogin.html")
