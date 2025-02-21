from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Routine)
admin.site.register(Exercise)
admin.site.register(RoutineExercise)
admin.site.register(RoutineSet)
admin.site.register(Workout)
admin.site.register(WorkoutExercise)
admin.site.register(WorkoutSet)