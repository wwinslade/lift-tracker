from django.shortcuts import render, redirect, get_object_or_404

from .forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import WorkoutTemplate, Workout, PredefinedExercise, CustomExercise, Exercise, ExerciseTemplate, Set, SetTemplate

# Home, also the default page
def home(request):
  return render(request, 'home.html')

@login_required()
def dashboard(request):
  return render(request, 'dashboard.html')

# Shows the user their defines workout templates
@login_required()
def WorkoutTemplatePage(request):
  workout_templates = WorkoutTemplate.objects.filter(user=request.user)
  return render(request, 'workout_templates.html', {'workout_templates': workout_templates})

# Shows the user detail on one of their specific workout templates
@login_required()
def WorkoutTemplateDetailPage(request, template_id):
  workout_template = get_object_or_404(WorkoutTemplate, id=template_id, user=request.user)
  exercise_templates = workout_template.exercisetemplate_set.all()

  context = {
    'workout_template': workout_template,
    'exercise_templates': exercise_templates,
  }
  
  return render(request, 'workout_template_detail.html', context)

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