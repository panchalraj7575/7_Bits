from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
# superuser = admin
# password = admin


class Employee(models.Model):
    emp_Id = models.AutoField(primary_key=True)
    emp_Name = models.CharField(max_length=40)
    emp_Department = models.CharField(max_length=40)

    def __str__(self):
        return self.emp_Name


class EmployeeSalary(models.Model):
    emp_Sal_Id = models.AutoField(primary_key=True)
    emp_Id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    emp_Salary = models.IntegerField()

    def __str__(self):
        return self.emp_Id.emp_Name


class AddCategory(models.Model):
    cat_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category
