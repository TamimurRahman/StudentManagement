
from django.urls import path
from .views import create_student,student_list,student_profile_view,update_student

urlpatterns = [
   path('create/',create_student,name='create'),
   path('',student_list,name='list'),
   path('profile/<int:id>',student_profile_view,name='st_profile_view'),
   path('update/<int:id>',update_student,name='update')
]
