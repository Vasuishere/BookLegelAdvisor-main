from django.shortcuts import render,redirect,get_object_or_404
from adminapp.models import lawyer,Education,Work_experience
from clientapp.models import clients,messages
from userapp.models import Appointment
from adminapp.forms import update_lawyer_profile
import random
from django.core.mail import send_mail
from django.conf import settings

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
    prof_ile = lawyer.objects.filter(id=name).values('name','email').first
    education = Education.objects.filter(lawyer=name).values('degree','institution','expertise','start_date','end_date').all().order_by('-end_date')
    experience = Work_experience.objects.filter(lawyer=name).values('Court','start_date','end_date').all()
    return render(request,'lawyerapp/profile.html',{'profile':prof_ile,'education':education,'experience':experience})


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
        obj = messages.objects.create(title=title, msg=msg, client=client, lawyer_name=lawyer_name)
        return redirect(f'/message/{id}')
    return render(request, 'lawyerapp/message.html', {'data': data, 'client': client,'data1':data1})


def forgotpassword(request):
    if request.method == 'POST':
        user_email = request.POST['email']
        try:
            lawyer_obj = lawyer.objects.get(email=user_email)
            random_no = ''.join([str(random.randint(0, 9)) for _ in range(6)])
            lawyer_obj.password = random_no
            lawyer_obj.save()
            message = f"Dear User,Here is your temporary password: {random_no}Please use this password to login to your account. We recommend changing your password after logging in.Thanks for reaching us!Best regards,From Admin Team"
            subject = 'Reset Password'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user_email]
            send_mail(subject, message, email_from, recipient_list)
            return redirect('/')
        except lawyer.DoesNotExist:
            return render(request, "lawyerapp/forgotpassword.html", {'error': 'Email not found'})
            
    return render(request, "lawyerapp/forgotpassword.html")

def changepassword(request):
    return render(request,"lawyerapp/changepassword.html")

def demo(request):
    random_no = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    return render(request,'lawyerapp/demo.html', {'random': random_no})