from multiprocessing import context
from django.shortcuts import render,redirect
from .models import login_data,contactus, stolenproperty
from .forms import contactForm,firForm,missingpForm, stolenForm
from django.contrib.auth import logout
from django.contrib.auth import authenticate, logout as auth_logout
from .models import fir as frr
from .models import missingperson as mpp
from .models import stolenproperty as stp

# Create your views here.

def index(request):
    if request.method=='POST':
        email_id=request.POST['email_id']
        passwrd=request.POST['passwrd']

        user=login_data.objects.filter(email_id=email_id,passwrd=passwrd)
        if user:
            print('Login Successfully')
            request.session['user']=email_id
            return redirect('/police')
        else:
            print('Login Failed.')
    
		
    return render (request,'index.html')

def contact(request):
    if request.method=='POST':
        ct=contactForm(request.POST)
        if ct.is_valid():
            ct.save()
        else:
            print(ct.errors)
    return render (request,'index.html')

def services(request):
    return render (request,'services.html')

def fir(request):
    if request.method=='POST':
        fr=firForm(request.POST)
        if fr.is_valid():
            fr.save()
        else:
            print(fr.errors)
    return render (request,'services.html')


def missingperson(request):
    if request.method=='POST':
        mp=missingpForm(request.POST)
        if mp.is_valid():
            mp.save()
        else:
            print(mp.errors)
    return render (request,'services.html')

def stolen(request):
    if request.method=='POST':
        st=stolenForm(request.POST)
        if st.is_valid():
            st.save()
        else:
            print(st.errors)
    return render (request,'services.html')

def police(request):
    user=request.session.get('user')
    fr=frr.objects.all()
    mp=mpp.objects.all()
    st=stp.objects.all()
    return render(request,'police.html',{'fr':fr,'mp':mp,'st':st,'user':user})

def logout(request):
    request.session.get('user')
    auth_logout(request)
    return redirect('/')