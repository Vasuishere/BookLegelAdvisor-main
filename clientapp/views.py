from django.shortcuts import render,redirect
from .models import clients,messages
from userapp.models import Appointment

# Create your views here.
def index(request):
    data1 = Appointment.objects.filter(userid=request.session["user_id"]).all()
    msg = messages.objects.filter(client=request.session["user_id"]).all()
    return render(request, 'clientapp/index.html', {"data1": data1,"msg":msg})


def login_view(request):
    if request.session.get("isclientlogin"):
        return redirect("/index")
    if request.POST:
        name = request.POST['name']
        password = request.POST['password']
        client = clients.objects.filter(name=name,password=password).values('id').first()
        if client != None:
            request.session['isclientlogin'] = True
            request.session['name'] = name
            request.session['user_id'] = client['id']
            return redirect('/index')
        else :
            return render(request,'clientapp/login.html',{'error':'Invalid username or password'})
    return render(request,'clientapp/login.html')

def logout(request):
    del request.session['isclientlogin']
    return redirect("/")



def appointment(request):
    if request.method == "POST":
        # Get the logged in client
        user_id = request.session.get('user_id')
        client = clients.objects.get(id=user_id)
        
        # Create appointment
        appointment = Appointment(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phoneno=request.POST.get("phoneno"),
            message=request.POST.get("message"),
            userid=client,  # Set the client foreign key
            lid=client.lid,  # Set the lawyer foreign key from client's relation
        )
        
        # Handle document upload
        if 'up_doc1' in request.FILES:
            appointment.up_doc1 = request.FILES['up_doc1']
        
        appointment.save()
        return redirect("/index")

    return render(request, "clientapp/appointment.html")


def details(request):
    return render(request,'clientapp/details.html')

def instruction(request):
    return render(request,'clientapp/instruction.html')

def login(request):
    return render(request,'clientapp/login.html')