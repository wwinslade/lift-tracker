# lifttrak/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('routines/', views.WorkoutTemplatePage, name='routines'),
    path('routines/<int:template_id>/', views.WorkoutTemplateDetailPage, name='routines_detail'),
    path('routines/create/', views.CreateWorkoutTemplate, name='create_routine'),
    path('login/', views.loginUserPage, name='login'),
    path('register/', views.registerUserPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
]