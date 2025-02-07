from django.shortcuts import render,redirect,get_object_or_404
from .models import lawyers
from adminapp.models import lawyer
from clientapp.models import clients,messages
from userapp.models import Appointment
from adminapp.forms import update_lawyer_profile

def login_lawyer(request):
    if request.session.get("islawyerlogin"):
        return redirect("/index")
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        lawyerData = lawyer.objects.filter(email=email,password=password).values('id','name').first()
        if lawyerData != None:
            request.session['islawyerlogin'] = True
            request.session['user_id'] = lawyerData['id']
            request.session['name'] = lawyerData['name']
            request.session['email'] = email
            return redirect("/index")
    return render(request,"lawyerapp/login.html")

def logout(request):
    del request.session['islawyerlogin']
    return redirect("/")


def index(request):
    lawyer_id = request.session['user_id']
    data = Appointment.objects.filter(lid=lawyer_id)
    return render(request, 'lawyerapp/index.html',{"data":data})

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

# def message(request,id):
#     data = clients.objects.get(id=id)
#     if request.POST:
#         msg = request.POST['msg']
#         title = request.POST['title']
#         obj = messages(msg=msg,title=title)
#         obj.save()
#         return redirect("message",id=id)
#     return render(request,'lawyerapp/message.html',{"data":data})

# def message(request,id):
#     lawyer_name = request.session.get('name')
#     # Fetch lawyer details
#     try:
#         data = lawyer.objects.get(name=lawyer_name)
#     except lawyer.DoesNotExist:
#         data = None  

#     client = get_object_or_404(clients, id=id)
#     if request.POST:
#         title = request.POST.get('title')
#         msg = request.POST.get('msg')
#         cname = request.POST.get('client')
#         obj = messages(title=title,msg=msg,client=cname)
#         obj.save()
#         return redirect('/lawyerapp/index')

#     return render(request, 'lawyerapp/message.html',{'data': data,'client':client})

def message(request, id):
    lawyer_name = request.session.get('name')
    
    # Fetch lawyer details
    try:
        data = lawyer.objects.get(name=lawyer_name)
    except lawyer.DoesNotExist:
        data = None  

    client = get_object_or_404(clients, id=id)  # Get client instance

    if request.method == "POST":
        title = request.POST.get('title')
        msg = request.POST.get('msg')

        # Ensure messages is using the model, not a conflicting module name
        obj = messages.objects.create(title=title, msg=msg, client=client)
        return redirect('/lawyerapp/index')

    return render(request, 'lawyerapp/message.html', {'data': data, 'client': client})


def demo(request):
    return render(request,'lawyerapp/demo.html')