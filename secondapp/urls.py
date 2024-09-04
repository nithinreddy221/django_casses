from django.urls import path
from . import views

urlpatterns = [
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/create/', views.create_teacher, name='create_teacher'),
    path('teachers/update/<int:pk>/', views.update_teacher, name='update_teacher'),
    path('teachers/delete/<int:pk>/', views.delete_teacher, name='delete_teacher'),
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.create_student, name='create_student'),
    path('students/update/<int:pk>/', views.update_student, name='update_student'),
    path('students/delete/<int:pk>/', views.delete_student, name='delete_student'),
]
