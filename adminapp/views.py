from django.shortcuts import render,redirect,get_object_or_404
from userapp.models import contact,Appointment,Attorneys,case_categories,Types_Law,Blog,case_studies,Client_Review,User_Appointment
from adminapp.models import adminuser,lawyer
from clientapp.models import clients
from .forms import Attorneys_edit_Form,case_categories_edit_Form,types_edit_Form,case_studies_Form,blog_edit_Form,add_lawyer,add_clients_forms,edit_user_appointments
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'adminapp/index.html')

def Show_contact(request):
    data = contact.objects.all
    return render(request,'adminapp/contact.html',{"data":data})

def Show_Appointment(request):
    data = Appointment.objects.all
    user_appointments = User_Appointment.objects.all
    return render(request,'adminapp/appointment.html',{"data":data,"User_Appointment":user_appointments})

def login(request):
    admin_session = request.session.get("admin_session", {})
    if admin_session.get("is_logged_in"):
        return redirect("adminapp/index")
    if request.method == "POST":  # Use request.method for correctness
        name = request.POST["name"]
        password = request.POST["password"]
        user = adminuser.objects.filter(name=name, password=password).count()
        if user > 0:
            request.session["admin_session"] = {
                "is_logged_in": True,
                "name": name
            }
            messages.success(request, "Login Successfully")
            return redirect("/adminapp/index")
        messages.error(request, "Wrong Username Or Password")
    return render(request, 'adminapp/login.html')

def logout_admin(request):
    if 'admin_session' in request.session:
        del request.session['admin_session']
    return redirect('/adminapp')

def blog(request):
    data = Blog.objects.all
    return render(request,'adminapp/blog.html',{"data":data})

def add_blog(request):
    if request.method == 'POST':
        form = blog_edit_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/adminapp/blog')
    else:
        form = blog_edit_Form()
    return render(request, 'adminapp/add_blog.html', {'form': form})

def edit_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        form = blog_edit_Form(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('/adminapp/blog')
    else:
        form = blog_edit_Form(instance=blog)
    return render(request, 'adminapp/add_blog.html', {'form': form})

def delete_blog(request, id):
    data = Blog.objects.get(id=id).delete()
    return redirect("/adminapp/blog")

def attorneys(request):
    data = Attorneys.objects.all
    return render(request,'adminapp/attorneys.html',{"data":data})

def case_catogory(request):
    data = case_categories.objects.all
    return render(request,'adminapp/case_categories.html',{"data":data})


def add_team(request):
    if request.method == 'POST':  
        form = Attorneys_edit_Form(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()
            messages.success(request,'New Member Is Added Succesfully ')
            return redirect('/adminapp/attorneys')  
    else:
        form = Attorneys_edit_Form()  
    return render(request, 'adminapp/add_team.html', {'form': form})

def edit_attorneys(request,id):
    attorneys_instance = get_object_or_404(Attorneys, pk=id)
    if request.method == 'POST':
        form = Attorneys_edit_Form(request.POST, request.FILES, instance=attorneys_instance)
        if form.is_valid():
            form.save()
            return redirect('/adminapp/attorneys')
    else:
        form = Attorneys_edit_Form(instance=attorneys_instance)
    return render(request, 'adminapp/add_team.html', {'form': form})


def delete_Attorneys(request,id):
    data = Attorneys.objects.get(id=id).delete()
    messages.error(request,'Member Deleted Succesfully')
    return redirect("/adminapp/attorneys")

def add_or_edit_case_categories(request, id=None):
    instance = get_object_or_404(case_categories, pk=id) if id else None
    if request.method == 'POST':
        form = case_categories_edit_Form(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()  
            return redirect('adminapp/case_categories')
    else:
        form = case_categories_edit_Form(instance=instance)

    context = {
        'form': form,
        'is_edit': id is not None  
    }
    return render(request, 'adminapp/add_case_categories.html',{"form":form})
        
def delete_case_categories(request,id):
    data = case_categories.objects.get(id=id).delete()
    return redirect("/adminapp/case_categories")

def types_Law(request):
    data = Types_Law.objects.all
    return render(request,'adminapp/types_Law.html',{"data":data})

def add_or_edit_types_law(request, id=None):
    instance = get_object_or_404(Types_Law, pk=id) if id else None
    if request.method == 'POST':
        form = types_edit_Form(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/adminapp/types_Law')
    else:
        form = types_edit_Form(instance=instance)

    context = {
        'form': form,
        'is_edit': id is not None  
    }
    return render(request, 'adminapp/add_types_law.html', {'form': form})


def delete_types_law(request,id):
    data = Types_Law.objects.get(id=id).delete()
    return redirect("/adminapp/types_Law")

def casestudies(request):
    data = case_studies.objects.all()
    return render(request,'adminapp/casestudies.html',{"data":data})

def add_or_edit_case_study(request, pk=None):
    instance = get_object_or_404(case_studies, pk=pk) if pk else None
    if request.method == "POST":
        form = case_studies_Form(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()  
            return redirect('/adminapp/case_studies')  
    else:
        form = case_studies_Form(instance=instance)

    context = {
        'form': form,
        'is_edit': pk is not None  
    }
    return render(request, 'adminapp/add_case_studies.html', context)

def reviews(request):
    data = Client_Review.objects.all
    return render(request,'adminapp/reviews.html',{"data":data})

def lawyers(request):
    data = lawyer.objects.all
    return render(request,'adminapp/lawyer.html',{"data":data})

def delete_lawyer(request,id):
    data = lawyer.objects.get(id=id).delete()
    return redirect(request,"adminapp/lawyer.html")

def add_new_lawyer(request):
    if request.method == 'POST':  
        form = add_lawyer(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect('/adminapp/lawyer')  
    else:
        form = add_lawyer()  
    return render(request, 'adminapp/add_lawyer.html', {'form': form})

def client(request):
    data = clients.objects.all()
    return render(request,'adminapp/clients.html',{"data":data})


def add_or_edit_client(request, pk=None):
    instance = get_object_or_404(clients, pk=pk) if pk else None
    if request.method == "POST":
        form = add_clients_forms(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()  
            return redirect('/adminapp/clients')  
    else:
        form = add_clients_forms(instance=instance)
        
        context = {
        'form': form,
        'is_edit': pk is not None  
    }
    return render(request, 'adminapp/add_client.html', context)

def delete_client(request,id):
    data = clients.objects.get(id=id).delete()
    return render(request, "adminapp/clients.html")

def edit_lawyer(request,id):
    lawyer_instance = get_object_or_404(lawyer, pk=id)
    if request.method == 'POST':
        form = add_lawyer(request.POST, request.FILES, instance=lawyer_instance)
        if form.is_valid():
            form.save()
            return redirect('/adminapp/lawyer')
    else:
        form = add_lawyer(instance=lawyer_instance)
    return render(request, 'adminapp/add_lawyer.html', {'form': form})

def edit_appointments(request,id):
    appointment_instance = get_object_or_404(User_Appointment, pk=id)
    if request.method =="POST":
        form = edit_user_appointments(request.POST,instance=appointment_instance)
        if form.is_valid():
            form.save()
            return redirect('/adminapp/appointment')
        else:
            return render(request, 'adminapp/edit_appointments.html',{'form':form})
    else:
        form = edit_user_appointments(instance=appointment_instance)
    return render(request,"adminapp/edit_user_appointments.html", {'form':form})

def demo(request):
    return render(request,'adminapp/demo.html')