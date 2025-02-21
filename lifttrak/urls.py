# lifttrak/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePage),
    path('home/', views.HomePage, name='home'),
    path('guest/', views.GuestHomePage, name='guest'),
    path('guest/routines', views.GuestDisplayWillsRoutines, name='guest_routines'),
    path('guest/routines/<int:routine_id>/', views.GuestDisplayWillsRoutinesDetail, name='guest_routines_detail'),
    path('dashboard/', views.DashboardPage, name='dashboard'),
    path('routines/', views.WorkoutTemplatePage, name='routines'),
    path('routines/<int:routine_id>/', views.RoutineDetailPage, name='routines_detail'),
    path('routines/create/', views.CreateWorkoutTemplate, name='create_routine'),
    path('routines/update/<int:routine_id>/', views.UpdateWorkoutTemplate, name='update_routine'),
    path('routines/delete/<int:routine_id>/', views.DeleteWorkoutTemplate, name='delete_routine'),
    path('login/', views.loginUserPage, name='login'),
    path('register/', views.registerUserPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('workout/', views.LiveWorkoutPage, name='live_workout'),
]