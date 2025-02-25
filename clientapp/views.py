from django.shortcuts import render, redirect
from .models import clients, messages
from userapp.models import Appointment
from adminapp.models import lawyer

def index(request):
    client_session = request.session.get("client_session", {})
    if not client_session.get("is_logged_in"):
        return redirect("/clientapp/login")
    client_id = client_session["client_id"]
    lawyer_id = client_session["lawyer_id"]
    data1 = Appointment.objects.filter(userid=client_id).all()
    msg = messages.objects.filter(client=client_id, lawyer_name=lawyer_id).order_by('-created_at')[:3]
    return render(request, 'clientapp/index.html', {"data1": data1, "msg": msg})

def login_client(request):
    client_session = request.session.get("client_session", {})
    if client_session.get("is_logged_in"):
        return redirect("/clientapp/index")
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']
        client = clients.objects.filter(name=name, password=password).values('id', 'lid').first()
        if client:
            request.session["client_session"] = {
                "is_logged_in": True,
                "name": name,
                "client_id": client['id'],
                "lawyer_id": client['lid']
            }
            return redirect("/clientapp/index")
        else:
            return render(request, 'clientapp/login.html', {'error': 'Invalid username or password'})
    return render(request, 'clientapp/login.html')

def logout_client(request):
    if 'client_session' in request.session:
        del request.session['client_session']
    return redirect('/clientapp')

def appointment(request):
    client_session = request.session.get("client_session", {})
    if not client_session.get("is_logged_in"):
        return redirect("/clientapp/login")
    if request.method == "POST":
        client_id = client_session["client_id"]
        client = clients.objects.get(id=client_id)
        appointment = Appointment(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phoneno=request.POST.get("phoneno"),
            message=request.POST.get("message"),
            userid=client,
            lid=client.lid,
        )
        if 'up_doc1' in request.FILES:
            appointment.up_doc1 = request.FILES['up_doc1']
        appointment.save()
        return redirect("/clientapp/index")
    return render(request, "clientapp/appointment.html")

def details(request):
    client_session = request.session.get("client_session", {})
    if not client_session.get("is_logged_in"):
        return redirect("/clientapp/login")
    client_id = client_session["client_id"]
    appData = Appointment.objects.filter(userid=client_id).values('name', 'message', 'lid_id', 'email', 'phoneno').first()
    if appData:
        lawyerdata = lawyer.objects.filter(id=appData['lid_id']).values('name').first()
        return render(request, 'clientapp/details.html', {'appData': appData, 'lawyerdata': lawyerdata})
    return render(request, 'clientapp/details.html', {'error': 'No appointment data found'})

def instruction(request):
    client_session = request.session.get("client_session", {})
    if not client_session.get("is_logged_in"):
        return redirect("/clientapp/login")
    return render(request, 'clientapp/instruction.html')