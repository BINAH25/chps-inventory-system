from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.html import strip_tags
from .models import *
from .forms import *

# Create your views here.
@login_required(login_url="chps:admin_login")   
def home(request):
    return render(request, 'home.html')

# *******************  EDIT PAGE VIEW *****************************
@login_required(login_url="chps:admin_login")   
def edit(request, pk):
    patient = Registration.objects.get(id=pk)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('chps:patients')
    else:
        form = RegistrationForm(instance=patient)
    context = {
        'form': form
    }
    return render(request, 'edit.html', context)

# *******************  DELETE PAGE VIEW *****************************
@login_required(login_url="chps:admin_login")   
def delete_patient(request, pk):
    patient = Registration.objects.get(id=pk)
    if request.method == 'POST':
        patient.delete()
        messages.success(request, 'Patient deleted successfully')
        return redirect('chps:home')
    context = {
        'patient': patient
    }
    return render(request, "delete.html", context)

# *******************  GETTING ALL PATIENTS PAGE VIEW *****************************
@login_required(login_url="chps:admin_login")   
def patients(request):
    patients = Registration.objects.all().order_by('id')
    context = {
        'patients':patients
    }
    return render(request, 'patients.html', context)

# ******************* GETTING A PATIENT DETAILS DYNAMICALLY PAGE VIEW *****************************
@login_required(login_url="chps:admin_login")   
def patient_detail(request,pk):
    patient = Registration.objects.get(id=pk)
    context = {
        'patient': patient
    }
    return render(request, 'details.html', context)

# *******************  CREATING THE REGISTRATION PAGE VIEW *****************************
def send(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " form successfully submitted")
            return redirect(request.META.get("HTTP_REFERER"))

        else:
            for field, error in form.errors.items():
                error = strip_tags(error)
                messages.error(request,f"{field}: {error}")
                return redirect(request.META.get("HTTP_REFERER"))



# ******************* SEARCH PAGE VIEW *****************************
@login_required(login_url="chps:admin_login")   
def search(request):
    if request.method == 'POST':
        kw = request.POST['keyword']
        result = Registration.objects.filter(registration=kw)
        print(result)
        context = {
            'result':result
        }
    return render(request,'search.html',context)

# ******************* ADMIN LOGIN  VIEW *****************************
def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None and user.is_staff and user.is_superuser:
            login(request, user)
            return redirect('chps:home')

        else:
            messages.error(request, "Invalid Credential")
            return redirect("chps:admin_login")

    return render(request, 'login.html')

# ******************* ADMIN LOGOUT  VIEW *****************************
def log_out(request):
    logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect("chps:admin_login")
