from django.shortcuts import render,redirect,get_object_or_404
from .models import lawyers
from adminapp.models import lawyer
from clientapp.models import clients
from userapp.models import Appointment
from adminapp.forms import update_lawyer_profile
from django.contrib import messages

def login_lawyer(request):
    if request.session.get("is_login"):
        return redirect("/index")
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        lawyerData = lawyer.objects.filter(email=email,password=password).values('id').first()
        if lawyerData != None:
            request.session['is_login'] = True
            request.session['user_id'] = lawyerData['id']
            request.session['email'] = email
            return redirect("/index")
    return render(request,"lawyerapp/login.html")

def logout(request):
    del request.session['is_login']
    return redirect("/")


def index(request):
    return render(request, 'lawyerapp/index.html')

def virtualappointment(request):
    return render(request,'lawyerapp/virtualappointment.html')

def profile(request):
    email = request.session.get("email")
    data = lawyer.objects.filter(email=email).first()
    return render(request,'lawyerapp/profile.html',{"data":data})

def profile_update(request,id):
    lawyer_instance = get_object_or_404(lawyer, id=id)
    if request.method == 'POST':
        form = update_lawyer_profile(request.POST, instance=lawyer_instance)
        if form.is_valid():
            form.save()
            return redirect('/profile')
    else:
        form = update_lawyer_profile(instance=lawyer_instance)
    return render(request,'lawyerapp/profile_update.html')


def activeclient(request):
    lawyer_id = request.session['user_id']
    data = clients.objects.filter(lid=lawyer_id)
    return render(request,'lawyerapp/activeclient.html',{"data":data})

def pricing(request):
    return render(request,'lawyerapp/pricing.html')

def appointment(request):
    lawyer_id = request.session['user_id']
    data = Appointment.objects.filter(lid=lawyer_id)
    return render(request,'lawyerapp/appointment.html',{"data":data})

def demo(request):
    return render(request,'lawyerapp/demo.html')