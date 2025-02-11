from django.shortcuts import render, redirect, get_object_or_404

from .forms import CreateUserForm, WorkoutTemplateForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import WorkoutTemplate, Workout, PredefinedExercise, CustomExercise, Exercise, ExerciseTemplate, Set, SetTemplate

# Home, also the default page
def home(request):
  return render(request, 'home.html')

def guest(request):
  return render(request, 'guest/guest.html')

def guest_display_wills_routines(request):
  user = get_object_or_404(User, username='wwinslade')
  workout_templates = WorkoutTemplate.objects.filter(user=user)
  return render(request, 'guest/wills_routines.html', {'workout_templates': workout_templates})

def guest_display_wills_routines_detail(request, template_id):
  user = get_object_or_404(User, username='wwinslade')
  workout_template = get_object_or_404(WorkoutTemplate, id=template_id, user=user)
  exercise_templates = workout_template.exercisetemplate_set.all()

  context = {
    'workout_template': workout_template,
    'exercise_templates': exercise_templates,
  }
  
  return render(request, 'guest/wills_routines_detail.html', context)

@login_required()
def dashboard(request):
  last_5_workouts = Workout.objects.filter(user=request.user).order_by('date')[:5]
  recent_workout_templates = WorkoutTemplate.objects.filter(user=request.user).order_by('-updated_at')[:3]
  
  context = {'last_5_workouts': last_5_workouts, 'recent_workout_templates': recent_workout_templates}

  return render(request, 'user/dashboard.html', context)

# Shows the user their defines workout templates
@login_required()
def WorkoutTemplatePage(request):
  workout_templates = WorkoutTemplate.objects.filter(user=request.user).order_by('-updated_at')
  return render(request, 'user/workout_templates.html', {'workout_templates': workout_templates})

# Shows the user detail on one of their specific workout templates
@login_required()
def WorkoutTemplateDetailPage(request, template_id):
  workout_template = get_object_or_404(WorkoutTemplate, id=template_id, user=request.user)
  exercise_templates = workout_template.exercisetemplate_set.all()

  context = {
    'workout_template': workout_template,
    'exercise_templates': exercise_templates,
  }
  
  return render(request, 'user/workout_template_detail.html', context)

@login_required()
def CreateWorkoutTemplate(request):
  form = WorkoutTemplateForm()
  
  if request.method == 'POST':
    form = WorkoutTemplateForm(request.POST)
    if form.is_valid():
      workout_template = form.save(commit=False)
      workout_template.user = request.user
      workout_template.save()
      return redirect('routines')

  context = {'form': form}
  return render(request, 'user/create_workout_template.html', context)

@login_required()
def UpdateWorkoutTemplate(request, template_id):
  workout_template = get_object_or_404(WorkoutTemplate, id=template_id, user=request.user)
  form = WorkoutTemplateForm(instance=workout_template)

  if request.method == 'POST':
    form = WorkoutTemplateForm(request.POST, instance=workout_template)
    if form.is_valid():
      form.save()
      return redirect('routines')

  context = {'form': form, 'template_name': workout_template.name}
  return render(request, 'user/update_workout_template.html', context)

@login_required()
def DeleteWorkoutTemplate(request, template_id):
  workout_template = get_object_or_404(WorkoutTemplate, id=template_id, user=request.user)
  context = {'template_name': workout_template.name, 'template_id': template_id}

  if request.method == 'POST':
    workout_template.delete()
    return redirect('routines')

  return render(request, 'user/delete_workout_routine.html', context)

# User management below
@login_required()
def registerUserPage(request):
  form = CreateUserForm()

  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')

  context = {'form': form}
  return render(request, 'register.html', context)

def loginUserPage(request):

  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      messages.info(request, 'Username OR password is incorrect')
   
  context = {}
  return render(request, 'login.html', context)

def logoutUser(request):
  logout(request)
  return redirect('home')