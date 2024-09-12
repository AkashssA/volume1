from django.shortcuts import get_object_or_404, redirect, render
from .models import Employee
from .forms import Employeeform

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'emp_list.html', {'employees': employees})

def add_employee(request):
    if request.method == 'POST':
        form = Employeeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emp_list')
    else:
        form = Employeeform()
    return render(request, 'add_emp.html', {'form': form})

def delete_emp(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('emp_list')
    return render (request, 'delete_emp.html', {'employee': employee})

def update_emp(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = Employeeform(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('emp_list')
    else:
        form = Employeeform(instance=employee)
    return render(request, 'update_emp.html', {'form': form})
