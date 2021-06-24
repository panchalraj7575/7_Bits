from django.shortcuts import redirect, render
from . models import Employee, EmployeeSalary, AddCategory
from django.http import HttpResponse, HttpResponseRedirect, response
from django.http import JsonResponse
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


def index(req):
    cat12 = AddCategory.objects.all()
    if req.method == "POST":
        name = req.POST.get('name')
        department = req.POST.get('department')
        salary = req.POST.get('salary1')
        check_emp = Employee.objects.filter(emp_Name=name)
        if check_emp:
            message = "This Employee is already exist"
            return render(req, 'app/index.html', {'message': message})
        else:
            Employee(emp_Name=name, emp_Department=department).save()
            var1 = Employee.objects.get(emp_Name=name)
            employeeId = var1
            if var1:
                message = "Employee Added Succesfully"
                EmployeeSalary(emp_Id=employeeId, emp_Salary=salary).save()
                cat12 = AddCategory.objects.all()
                return render(req, 'app/index.html', {'message1': message, 'category': cat12})
    return render(req, 'app/index.html', {'category': cat12})


def showEmployee(req):
    data = EmployeeSalary.objects.all()
    return render(req, 'app/show.html', {'data': data})


def deleteEmployee(req):
    Id = req.GET['id']
    Employee.objects.filter(emp_Id=Id).delete()
    return redirect('showEmployee')


def editEmployee(request):
    Id = request.GET['id']
    cat12 = AddCategory.objects.all()
    for data in EmployeeSalary.objects.filter(emp_Id=Id):
        name = data.emp_Id.emp_Name
        salary = data.emp_Salary
        department = data.emp_Id.emp_Department
    return render(request, 'app/edit.html', {'id': Id, 'category': cat12, 'name': name, 'salary': salary, 'department': department})


def editEmployee2(req):
    if req.method == "POST":
        id = req.POST.get('id1')
        name = req.POST.get('name')
        department = req.POST.get('department')
        salary = req.POST.get('salary')
        Employee.objects.filter(emp_Id=id).update(
            emp_Name=name, emp_Department=department)
        var1 = Employee.objects.get(emp_Name=name)
        employeeId = var1
        if var1:
            EmployeeSalary.objects.filter(
                emp_Id=employeeId).update(emp_Salary=salary)
            return redirect('showEmployee')
    return render(req, 'app/edit.html')


def addCategory(req):
    if req.method == "POST":
        categoryName = req.POST.get('cname')
        check_cat = AddCategory.objects.filter(category=categoryName)
        if check_cat:
            message = "This Category is already exist"
            return render(req, 'app/addCategory.html', {'message': message})
        else:
            message = "Employee Added Succesfully"
            AddCategory(category=categoryName).save()

            return render(req, 'app/addCategory.html', {'message1': message})
    return render(req, 'app/addCategory.html')



# -------------- Api View ------------------
@api_view(['GET'])
def SHOWEMPLOYEE(req):
    if req.method == "GET":
        results = Employee.objects.all()
        serialize = EmployeeSerializer(results,many = True)
        return Response(serialize.data)