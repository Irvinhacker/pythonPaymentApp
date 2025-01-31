from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import *


def home(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            option = request.POST.get('options')
            customerid = request.POST.get('customerid')
            if option == 'prepaid':                
                return redirect(f'/prepaid/{option}/{customerid}')
            elif option == 'postpaid':
                return redirect(f'/postpaid/{option}/{customerid}')
            elif option == 'dth':
                return redirect(f'/dth/{option}/{customerid}')
            elif option == 'wifi':
                return redirect(f'/wifi/{option}/{customerid}')

            else:
                return redirect('/login')    
              
        else:
            return redirect('/login')
    else:    
    
        return render(request,'index.html')

def userlogin(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('userpassword')
        userlogin = authenticate(request,username=username,password=password)
        if userlogin is not None:
            login(request, userlogin)
            return redirect('/')
        else:
            messages.info(request,'Invalid username or password')
            return redirect('/login')
    else:    
        return render(request,'login.html')
    
def userlogout(request):
    logout(request)
    return redirect('/')

def usersignup(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        email=request.POST.get('useremail')
        password = request.POST.get('userpassword')
        confirmpassword = request.POST.get('userconfirmpassword')
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('/signup')
            else:
            # create user
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('/login')
        else:
            messages.info(request,'Password not matching')
            return redirect('/signup')
    
    return render(request,'signup.html')

def prepaidpage(request,option,customerid):
    
    plan = Prepaid.objects.all()     
    
    return render(request,'prepaid.html',{'option':option,'customerid':customerid,"plans":plan})

def postpaidpage(request,option,customerid):
    
    if (customerid == "8838615485"):
        plan = 58
    elif (customerid == "8838615486"):
        plan = 100
    elif (customerid == "8838615487"):
        plan = 126
    elif (customerid == "8838615488"):
        plan = 72
    elif (customerid == "8838615489"):
        plan = 277
    else:
        plan = "There are no bills for this number"
    
    return render(request,'postpaid.html',{'option':option,'id':customerid,"plans":plan})

def dthpage(request,option,customerid): 
    
    return render(request,'dth.html',{'option':option,'id':customerid})

def wifipage(request,option,customerid):
    
    plan = Wifi.objects.all()
    
    return render(request,'wifi.html',{'option':option,'customerid':customerid,"plans":plan})


def paymentgateway(request,option,customerid,id):
    
    if request.method == 'POST':
        Carddetails.cardname
        Carddetails.cardnumber
        Carddetails.cardexpiry
        Carddetails.cardcvv
        
    
    if option == 'prepaid':
        plans = Prepaid.objects.get(id=id)
    elif option == 'wifi':
        plans = Wifi.objects.get(id=id)
    
    
    return render(request,'paymentgateway.html',{'plans':plans,'customerid':customerid,'option':option})

