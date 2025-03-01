from django.shortcuts import render, redirect
from .models import clients, messages, Case
from userapp.models import Appointment
from adminapp.models import lawyer


def index(request):
    client_session = request.session.get("client_session", {})
    if not client_session.get("is_logged_in"):
        return redirect("clientapp:login_client")
    client_id = client_session["client_id"]
    lawyer_id = client_session["lawyer_id"]
    data1 = Appointment.objects.filter(userid=client_id).all()
    msg = messages.objects.filter(client=client_id, lawyer_name=lawyer_id).order_by('-created_at')[:3]
    return render(request, 'clientapp/index.html', {"data1": data1, "msg": msg})

def login_client(request):
    client_session = request.session.get("client_session", {})
    if client_session.get("is_logged_in"):
        return redirect("clientapp:index")
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
            return redirect("clientapp:index")
        else:
            return render(request, 'clientapp/login.html', {'error': 'Invalid username or password'})
    return render(request, 'clientapp/login.html')

def logout_client(request):
    if 'client_session' in request.session:
        del request.session['client_session']
    return redirect("clientapp:login_client")

def appoin_tment(request):
    client_session = request.session.get("client_session", {})
    if not client_session.get("is_logged_in"):
        return redirect("clientapp:login_client")
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
        return redirect("clientapp:index")
    return render(request, "clientapp/appointment.html")

def details(request):
    client_session = request.session.get("client_session", {})
    if not client_session.get("is_logged_in"):
        return redirect("clientapp:login_client")
    client_id = client_session["client_id"]
    appData = Appointment.objects.filter(userid=client_id).values('name', 'message', 'lid_id', 'email', 'phoneno').first()
    appData2 = Case.objects.filter(client=client_id).values('description').first()
    if appData:
        lawyerdata = lawyer.objects.filter(id=appData['lid_id']).values('name').first()
        return render(request, 'clientapp/details.html', {'appData': appData2, 'lawyerdata': lawyerdata})
    return render(request, 'clientapp/details.html', {'error': 'No appointment data found'})

def instruction(request):
    client_session = request.session.get("client_session", {})
    if not client_session.get("is_logged_in"):
        return redirect("clientapp:login_client")
    client_id = client_session["client_id"]
    lawyer_id = client_session["lawyer_id"]
    msg = messages.objects.filter(client=client_id, lawyer_name=lawyer_id).order_by('-created_at')[:3]
    return render(request, 'clientapp/instruction.html', {"msg": msg})

from django.shortcuts import render, redirect

def newcase_view(request):
    client_id = request.session.get('client_session', {}).get('client_id', 'id')
    appointments = Appointment.objects.filter(userid_id=client_id, status='completed')
    
    if request.method == 'POST':
        try:
            # Get form data
            appointment_id = request.POST.get('appointmentHistory')
            description = request.POST.get('description')
            document = request.FILES.get('document')
            
            # Validate required fields
            if not appointment_id or not description:
                return render(request, 'clientapp/newcase.html', {'appointments': appointments})
            
            # Get the appointment object
            appointment = Appointment.objects.get(id=appointment_id, userid_id=client_id)
            
            # Create and save new case
            new_case = Case(
                client_id=client_id,
                appointment=appointment,
                description=description,
            )
            
            # Handle file upload if present
            if document:
                new_case.document = document
                
            new_case.save()
            
            return redirect('clientapp:index')
            
        except Appointment.DoesNotExist:
            return render(request, 'clientapp/newcase.html', {'appointments': appointments})
        except Exception as e:
            return render(request, 'clientapp/newcase.html', {'appointments': appointments})
    
    context = {
        'appointments': appointments
    }
    return render(request, 'clientapp/newcase.html', context)

