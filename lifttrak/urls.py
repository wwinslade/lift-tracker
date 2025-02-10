# lifttrak/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),
    path('guest/', views.guest, name='guest'),
    path('guest/routines', views.guest_display_wills_routines, name='guest_routines'),
    path('guest/routines/<int:template_id>/', views.guest_display_wills_routines_detail, name='guest_routines_detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('routines/', views.WorkoutTemplatePage, name='routines'),
    path('routines/<int:template_id>/', views.WorkoutTemplateDetailPage, name='routines_detail'),
    path('routines/create/', views.CreateWorkoutTemplate, name='create_routine'),
    path('login/', views.loginUserPage, name='login'),
    path('register/', views.registerUserPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
]