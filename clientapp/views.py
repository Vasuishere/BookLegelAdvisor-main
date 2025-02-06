from django.shortcuts import render,redirect
from .models import clients
from userapp.models import Appointment

# Create your views here.
def index(request):
    data1 = Appointment.objects.filter(userid=request.session["user_id"]).all()  # ✅ Corrected
    return render(request, 'clientapp/index.html', {"data1": data1})


def login_view(request):
    if request.session.get("islogin"):
        return redirect("index")
    if request.POST:
        name = request.POST['name']
        password = request.POST['password']
        client = clients.objects.filter(name=name,password=password).values('id').first()
        if client != None:
            request.session['islogin'] = True
            request.session['name'] = name
            request.session['user_id'] = client['id']
            return redirect('index')
        else :
            return render(request,'clientapp/login.html',{'error':'Invalid username or password'})
    return render(request,'clientapp/login.html')

def logout(request):
    del request.session['islogin']
    return redirect("/")

# def appointment(request):
#     if request.method == "POST":  
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         phoneno = request.POST.get("phoneno")
#         message = request.POST.get("message")
#         up_doc1 = request.FILES.get("up_doc1")
#         user_id = request.session['user_id']
#         obj = Appointment(name=name, email=email, phoneno=phoneno, message=message, up_doc1=up_doc1,userid_id=user_id)
#         obj.save()
#         return redirect("clientapp/index")  
    # return render(request, "clientapp/appointment.html")
def appointment(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phoneno = request.POST.get("phoneno")
        message = request.POST.get("message")
        up_doc1 = request.FILES.get("up_doc1")
        user_id = request.session['user_id']

        # Fetch the client based on session user_id
        client = clients.objects.get(id=user_id)
        lawyer_name = client.lid.name  # Fetching lawyer's name from the ForeignKey field

        # Save appointment
        obj = Appointment(
            name=name, 
            email=email, 
            phoneno=phoneno, 
            message=message, 
            up_doc1=up_doc1, 
            userid_id=user_id, 
            lawyer=lawyer_name  # Store lawyer's name
        )
        obj.save()
        return redirect("clientapp/index")

    return render(request, "clientapp/appointment.html")


def details(request):
    return render(request,'clientapp/details.html')

def instruction(request):
    return render(request,'clientapp/instruction.html')

def login(request):
    return render(request,'clientapp/login.html')