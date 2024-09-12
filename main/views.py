from django.shortcuts import render, redirect
from .models import Employee
from .forms import Employeeform

# Create your views here.
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'emp_list.html', {'employees': employees})

def add_employee(request):
    if request.method == 'POST':
        form = Employeeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emp_list')  # Ensure this matches the name in your URL patterns
    else:
        form = Employeeform()
    
    return render(request, 'add_emp.html', {'form': form})
