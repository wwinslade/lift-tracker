from django.contrib import admin
from .models import WorkoutTemplate, Workout, PredefinedExercise, CustomExercise, Exercise, ExerciseTemplate, Set, SetTemplate

# Register your models here.
admin.site.register(WorkoutTemplate)
admin.site.register(Workout)
admin.site.register(PredefinedExercise)
admin.site.register(CustomExercise)
admin.site.register(Exercise)
admin.site.register(ExerciseTemplate)
admin.site.register(Set)
admin.site.register(SetTemplate)