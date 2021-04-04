import csv
from django.shortcuts import render,redirect    
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import *   
from .forms import EmployeeUpdateForm, CreateUserForm
from django.views.generic import DeleteView
from django.contrib.auth.decorators import login_required

# Create your views here.
def export(request, pk1):
    emp = Employee.objects.get(id=pk1)
    tasks = emp.task_set.all()
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['Employee Name','Employee Phone','Employee Adress'])
    writer.writerow([emp.user.username,emp.phone,emp.adress])
    for task in tasks.values_list('task'):
        writer.writerow(task)
    response['Content-Disposition'] = 'filename="employeedata.csv"'
    return response

def welcome(request):
    user = request.user
    return render(request, 'employees/welcome.html',{'user':user})

def adminpage(request):
    emps = Employee.objects.all()
    return render(request,'employees/admin_dashboard.html',{'emps':emps})

def registerPage(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            return redirect('login')

    context={'form':form}
    return render(request,'employees/register.html',context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard',user.employee.id)
    return render(request, 'employees/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url="login")
def tasks(request, pk1):
    emp = Employee.objects.get(id=pk1)
    tasks = emp.task_set.all()

    return render(request, 'employees/dashboard.html',{'tasks':tasks})
@login_required(login_url="login")

def profile(request, pk):
    user = request.user
    if request.method == 'POST':
        p_form = EmployeeUpdateForm(request.POST,request.FILES, instance=request.user.employee)
        if p_form.is_valid():
            p_form.save()
            return redirect('profile',user.employee.id)

    else:
        p_form = EmployeeUpdateForm(instance=request.user.employee)


    emp = Employee.objects.get(id=pk)
 
    context = {
        'p_form':p_form,
        'emp':emp,
        
    }
    return render(request,'employees/profile.html',context)
@login_required(login_url="login")

def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    user = request.user
    if request.method == "POST":
        task.delete()
        return redirect('dashboard',user.employee.id)
    context={
        'task':task,
        'user':user
    }
    return render(request, 'employees/delete.html',context)
    