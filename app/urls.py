from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('showEmployee/', views.showEmployee, name="showEmployee"),
    path('delete/', views.deleteEmployee, name="deleteEmployee"),
    path('edit/', views.editEmployee, name="editEmployee"),
    path('recordedited/', views.editEmployee2, name="editEmployee2"),
    path('addCategory/', views.addCategory, name='addCategory'),

    # -------------- Api url ------------------
    path('SHOW/', views.SHOWEMPLOYEE, name="SHOWEMPLOYEE"),

]
