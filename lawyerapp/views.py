from django.shortcuts import render,redirect,get_object_or_404
from adminapp.models import lawyer,Education
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
    name = request.session['user_id']
    profile = lawyer.objects.filter(name=name).values('name','email').first
    education = Education.objects.filter(lawyer=name).values('degree').first
    return render(request,'lawyerapp/profile.html',{'profile':profile,'education':education})


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


def message(request, id):
    data1 = messages.objects.filter(lawyer_name_id=request.session["user_id"],client_id=id).all().order_by('-created_at')
    lawyer_name = request.session.get('name')
    
    # Fetch lawyer details
    try:
        data = lawyer.objects.get(name=lawyer_name)
    except lawyer.DoesNotExist:
        data = None  
    client = get_object_or_404(clients, id=id)  # Get client instance
    lawyer_name = data
    if request.method == "POST":
        title = request.POST.get('title')
        msg = request.POST.get('msg')

        # Ensure messages is using the model, not a conflicting module name
        obj = messages.objects.create(title=title, msg=msg, client=client, lawyer_name=lawyer_name)
        return redirect(f'/message/{id}')

    return render(request, 'lawyerapp/message.html', {'data': data, 'client': client,'data1':data1})


def demo(request):
    return render(request,'lawyerapp/demo.html')