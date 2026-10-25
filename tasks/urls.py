from django.urls import path
from . import views

urlpatterns=[
    path('', views.task_list, name='task_list'),
    path('add/form/', views.add_task_form, name='add_task_form'),
    path('add/', views.add_task, name='add_task'),
    path('delete_task/', views.delete_task, name='delete_task'),
]