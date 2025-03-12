from django.shortcuts import render, redirect, get_object_or_404

from .forms import CreateUserForm, RoutineForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import Routine, Exercise, RoutineExercise, RoutineSet, Workout, WorkoutExercise, WorkoutSet

from django.http import JsonResponse


# Home, also the default page
def HomePage(request):
  return render(request, 'home.html')

def GuestHomePage(request):
  return render(request, 'guest/guest.html')

def GuestDisplayWillsRoutines(request):
  user = get_object_or_404(User, username='wwinslade')
  routines = Routine.objects.filter(user=user)
  return render(request, 'guest/wills_routines.html', {'routines': routines})

def GuestDisplayWillsRoutinesDetail(request, routine_id):
  user = get_object_or_404(User, username='wwinslade')
  routine = get_object_or_404(Routine, id=routine_id, user=user)
  routine_exercises = RoutineExercise.objects.filter(routine=routine).prefetch_related('sets').order_by('order')
  context = {
    'routine': routine,
    'routine_exercises': routine_exercises,
  }
  
  return render(request, 'guest/wills_routines_detail.html', context)

@login_required()
def DashboardPage(request):
  last_5_workouts = Workout.objects.filter(user=request.user).order_by('date')[:5]
  recent_routines = Routine.objects.filter(user=request.user).order_by('-updated_at')[:3]
  
  context = {'last_5_workouts': last_5_workouts, 'recent_routines': recent_routines}

  return render(request, 'user/dashboard.html', context)

# Shows the user their defines workout templates
@login_required()
def RoutinesPage(request):
  routines = Routine.objects.filter(user=request.user).order_by('-updated_at')
  return render(request, 'user/routines_list.html', {'routines': routines})

# Shows the user detail on one of their specific workout templates
@login_required()
def RoutineDetailPage(request, routine_id):
  routine = get_object_or_404(Routine, id=routine_id, user=request.user)
  routine_exercises = RoutineExercise.objects.filter(routine=routine).prefetch_related('sets').order_by('order')
  context = {
    'routine': routine,
    'routine_exercises': routine_exercises,
  }
  
  return render(request, 'user/workout_template_detail.html', context)

@login_required()
def CreateWorkoutTemplate(request):
  form = RoutineForm()
  
  if request.method == 'POST':
    form = RoutineForm(request.POST)
    if form.is_valid():
      routine = form.save(commit=False)
      routine.user = request.user
      routine.save()
      return redirect('routines')

  context = {'form': form}
  return render(request, 'user/create_workout_template.html', context)

@login_required()
def UpdateWorkoutTemplate(request, template_id):
  routine = get_object_or_404(Routine, id=template_id, user=request.user)
  form = RoutineForm(instance=routine)

  if request.method == 'POST':
    form = RoutineForm(request.POST, instance=routine)
    if form.is_valid():
      form.save()
      return redirect('routines')

  context = {'form': form, 'template_name': routine.name}
  return render(request, 'user/update_workout_template.html', context)

@login_required()
def DeleteWorkoutTemplate(request, template_id):
  routine = get_object_or_404(Routine, id=template_id, user=request.user)
  context = {'template_name': routine.name, 'template_id': template_id}

  if request.method == 'POST':
    routine.delete()
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

@login_required()
def CreateWorkout(request):
  workout = Workout.objects.create(user=request.user)
  exercises = Exercise.objects.all()

  if request.method == 'POST':
    if 'add_exercise' in request.POST:
      exercise_id = request.POST.get('exercise_id')
      exercise = get_object_or_404(Exercise, id=exercise_id)
      order = request.POST.get('order', 0)  # Default to 0 if not provided
      description = request.POST.get('description', exercise.description)  # Default to parent exercise if not specified
      workout_exercise = WorkoutExercise.objects.create(workout=workout, exercise=exercise, order=order, description=description)
      return redirect('add_sets', workout_id=workout.id)

  context = {
    'workout': workout,
    'exercises': exercises,
  }

  return render(request, 'user/create_workout.html', context)
