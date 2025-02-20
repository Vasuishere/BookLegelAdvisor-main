from django.shortcuts import render,redirect
from .models import clients,messages
from userapp.models import Appointment
from adminapp.models import lawyer

# Create your views here.
def index(request):
    lawyer_id = request.session.get("lawyer_id")
    data1 = Appointment.objects.filter(userid=request.session["user_id"]).all()
    msg = messages.objects.filter(client=request.session["user_id"],lawyer_name=lawyer_id).order_by('-created_at')[:3]
    return render(request, 'clientapp/index.html', {"data1": data1,"msg":msg})


def login_view(request):
    if request.session.get("isclientlogin"):
        return redirect("clientapp/index")
    if request.POST:
        name = request.POST['name']
        password = request.POST['password']
        client = clients.objects.filter(name=name,password=password).values('id','lid').first()
        if client != None:
            request.session['isclientlogin'] = True
            request.session['name'] = name
            request.session['user_id'] = client['id']
            request.session['lawyer_id'] = client['lid']
            return redirect('clientapp/index')
        else :
            return render(request,'clientapp/login.html',{'error':'Invalid username or password'})
    return render(request,'clientapp/login.html')

def logout(request):
    del request.session['isclientlogin']
    return redirect("/clientapp")



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
        return redirect("/clientapp/index")

    return render(request, "clientapp/appointment.html")


def details(request):
    userId = request.session.get('user_id')
    appData = Appointment.objects.filter(userid=userId).values('name','message','lid_id','email','phoneno').first()
    if appData is not None:
        lawyerdata = lawyer.objects.filter(id=appData['lid_id']).values('name').first()
        return render(request,'clientapp/details.html',{'appData':appData,'lawyerdata':lawyerdata})

def instruction(request):
    return render(request,'clientapp/instruction.html')

def login(request):
    return render(request,'clientapp/login.html')