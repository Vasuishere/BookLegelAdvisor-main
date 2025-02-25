from django.shortcuts import render,redirect,get_object_or_404
from adminapp.models import lawyer,Education,Work_experience
from clientapp.models import clients,messages
from userapp.models import Appointment,User_Appointment
from adminapp.forms import update_lawyer_profile
import random
from django.core.mail import send_mail
from django.conf import settings
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required

def login_lawyer(request):
    lawyer_session = request.session.get("lawyer_session", {})
    if lawyer_session.get("is_logged_in"):
        return redirect("/lawyerapp/index")
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        lawyerData = lawyer.objects.filter(email=email, password=password).values('id', 'name').first()
        if lawyerData:
            request.session["lawyer_session"] = {
                "is_logged_in": True,
                "lawyer_id": lawyerData['id'],
                "name": lawyerData['name'],
                "email": email
            }
            return redirect("/lawyerapp/index")
    return render(request, "lawyerapp/login.html")

def logout_lawyer(request):
    if 'lawyer_session' in request.session:
        del request.session['lawyer_session']
    return redirect('/lawyerapp')


def index(request):
    lawyer_session = request.session.get("lawyer_session", {})
    lawyer_id = lawyer_session.get("lawyer_id")
    
    if not lawyer_id:
        return redirect("/lawyerapp/login")
        
    data = Appointment.objects.filter(lid=lawyer_id)
    User_appointments = User_Appointment.objects.filter(lawyer=lawyer_id)
    
    return render(request, 'lawyerapp/index.html', {
        "data": data,
        "User_appointments": User_appointments
    })

@login_required
def google_login_callback(request):
    try:
        social_account = SocialAccount.objects.get(user=request.user)
        lawyer_data = lawyer.objects.filter(email=request.user.email).first()
        if lawyer_data:
            request.session["lawyer_session"] = {
                "is_logged_in": True,
                "lawyer_id": str(lawyer_data.id),
                "name": str(lawyer_data.name),
                "email": str(request.user.email)
            }
            request.session.modified = True
            return redirect("/lawyerapp/index")
        else:
            messages.error(request, "No lawyer account found with this email")
            return redirect("/")
    except Exception as e:
        messages.error(request, "Error during Google login")
        return redirect("/")
    
def virtualappointment(request):
    return render(request,'lawyerapp/virtualappointment.html')


def profile(request):
    lawyer_session = request.session.get("lawyer_session", {})
    name = lawyer_session.get("lawyer_id")
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
    lawyer_session = request.session.get("lawyer_session", {})
    lawyer_id = lawyer_session.get("lawyer_id")
    data = clients.objects.filter(lid=lawyer_id)
    return render(request,'lawyerapp/activeclient.html',{"data":data})

def pricing(request):
    return render(request,'lawyerapp/pricing.html')

def appointment(request):
    lawyer_session = request.session.get("lawyer_session", {})
    lawyer_id = lawyer_session.get("lawyer_id")
    if not lawyer_id:
        return redirect("/lawyerapp/login")
    data = Appointment.objects.filter(lid=lawyer_id)
    User_appointments = User_Appointment.objects.filter(lawyer=lawyer_id)
    return render(request, 'lawyerapp/appointment.html', {
        "data": data,
        "User_appointments": User_appointments  # Fixed key name
    })


def message(request, id):
    lawyer_session = request.session.get("lawyer_session", {})
    lawyer_id = lawyer_session.get("lawyer_id")
    if not lawyer_id:
        return redirect("/lawyerapp/login")
    data1 = messages.objects.filter(lawyer_name_id=lawyer_id, client_id=id).all().order_by('-created_at')
    lawyer_name = lawyer_session.get("name")  # Fetch from session dict
    
    try:
        data = lawyer.objects.get(id=lawyer_id)  # Use ID instead of name
    except lawyer.DoesNotExist:
        data = None  
    client = get_object_or_404(clients, id=id)
    lawyer_name = data
    if request.method == "POST":
        title = request.POST.get('title')
        msg = request.POST.get('msg')
        obj = messages.objects.create(title=title, msg=msg, client=client, lawyer_name=lawyer_name)
        obj.save()
        return redirect(f'/lawyerapp/message/{id}/')
    return render(request, 'lawyerapp/message.html', {'data': data, 'client': client, 'data1': data1})


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
