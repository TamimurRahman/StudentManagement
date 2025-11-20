
from django.urls import path
from .views import create_student,student_list

urlpatterns = [
   path('create/',create_student,name='create'),
   path('',student_list,name='list')
]
