from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

from myapp.forms import library_login, library_faculty, library_student
from myapp.models import Login_view, Faculty, Student


# Create your views here.
def home(request):
    return render(request, 'home.html')
def dashboard(request):
    return render(request, 'dashboard.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admindash')
            elif user.is_faculty:
                return redirect('facultydash')
            elif user.is_student:
                return redirect('studentdash')

        else:
            messages.info(request, 'Invalid Credentials')

    return render(request, 'login.html')



def reg_faculty(request):
    form1 = library_login()
    form2 = library_faculty()
    if request.method == 'POST':
        form1 = library_login(request.POST)
        form2 = library_faculty(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            a = form1.save(commit=False)
            a.is_faculty = True
            a.save()
            user1 = form2.save(commit=False)
            user1.user = a
            user1.save()
            return redirect("/")

    return render(request, 'Registration.html', {'formkey1': form1, 'formkey2': form2})


def reg_student(request):
    form1 = library_login()
    form2 = library_student()
    if request.method == 'POST':
        form1 = library_login(request.POST)
        form2 = library_student(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            a = form1.save(commit=False)
            a.is_student = True
            a.save()
            user1 = form2.save(commit=False)
            user1.user = a
            user1.save()
            return redirect("/")

    return render(request, 'student_Registration.html', {'formkey1': form1, 'formkey2': form2})

def admindash(request):
    return render(request, 'admin_dash/admindashboard.html')


def facultydash(request):
    return render(request, 'staff_dash/staffdashboard.html')


def studentdash(request):
    return render(request, 'student_dash/studentdashboard.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admindash')
            elif user.is_faculty:
                return redirect('facultydash')
            elif user.is_student:
                return redirect('studentdash')

        else:
            messages.info(request, 'Invalid Credentials')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('loginpage')
