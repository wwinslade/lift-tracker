from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import WorkoutTemplate, ExerciseTemplate, SetTemplate, Workout, Exercise, Set, CustomExercise, PredefinedExercise

class CreateUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class WorkoutTemplateForm(ModelForm):
  class Meta:
    model = WorkoutTemplate
    fields = ['name', 'description']