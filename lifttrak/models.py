from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Templates for workouts
class WorkoutTemplate(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

# For actual workouts based on templates
class Workout(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  template = models.ForeignKey(WorkoutTemplate, on_delete=models.CASCADE)
  date = models.DateTimeField(auto_now_add=True)

# For predefined exercises that are globally available
class PredefinedExercise(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField()
  muscles_targeted = models.CharField(max_length=255)

# For custom exercises that users can create
class CustomExercise(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  description = models.TextField()
  muscles_targeted = models.CharField(max_length=255)

# For exercises in workouts, either from predefined global or custom
class Exercise(models.Model):
  workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="exercises")

  content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
  object_id = models.PositiveIntegerField()
  content_object = GenericForeignKey('content_type', 'object_id')

# For templates of exercises
class ExerciseTemplate(models.Model):
  template = models.ForeignKey(WorkoutTemplate, on_delete=models.CASCADE)
  predefined_exercise = models.ForeignKey(PredefinedExercise, on_delete=models.CASCADE, null=True, blank=True)
  custom_exercise = models.ForeignKey(CustomExercise, on_delete=models.CASCADE, null=True, blank=True)
  name = models.CharField(max_length=255)
  pinned_notes = models.TextField()

class SetTemplate(models.Model):
  exercise_template = models.ForeignKey(ExerciseTemplate, on_delete=models.CASCADE)
  set_number = models.IntegerField()
  reps = models.IntegerField()
  weight = models.FloatField(default=0.0)
  rir = models.IntegerField(default=3)

# For individual set tracking
class Set(models.Model):
  exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="sets")
  set_number = models.IntegerField()
  reps = models.IntegerField()
  weight = models.FloatField(default=0.0)
  rir = models.IntegerField(default=3)
  completed_at = models.DateTimeField(auto_now_add=True)
