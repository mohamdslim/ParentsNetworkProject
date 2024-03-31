from django.contrib import admin
from django.urls import path , include
from .views import *
from . import views
urlpatterns = [
 path('',login_page,name='login'),
 path('signup/' , SignupView.as_view(),name='signup'),
 path('logout/',logout_user,name='logout'),
 path('profile/',profile,name='profile'),
 path('account-settings/',AccountSettingsView.as_view(),name='account-settings'),


 path('addParent/', views.addParent, name='addParent'),
 path('deleteParent/<str:pk>', views.deleteParent, name='deleteParent'),

 path('toDoList/', views.toDoList, name='toDoList'),
 path('add_task/', views.addTask, name='add_task'),
 path('delete_task/<str:pk>', views.deleteTask, name='delete_task'),
]
