from django.contrib import admin
from .models import Employee, EmployeeSalary,AddCategory
# Register your models here.
admin.site.register(Employee)
admin.site.register(EmployeeSalary)
admin.site.register(AddCategory)
