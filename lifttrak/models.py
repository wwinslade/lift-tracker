from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Templates for workouts
class WorkoutTemplate(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  description = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.user.username}.{self.name}"

# For actual workouts based on templates
class Workout(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  template = models.ForeignKey(WorkoutTemplate, on_delete=models.CASCADE)
  notes = models.TextField(null=True, blank=True)
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.user.username}.{self.template.name}.{self.date}"

# For predefined exercises that are globally available
class PredefinedExercise(models.Model):
  muscles_targeted_choices = [
    ('chest', 'Chest'),
    ('traps', 'Traps'),
    ('rhomboids', 'Rhomboids'),
    ('lats', 'Lats'),
    ('lower_back', 'Lower Back'),
    ('quadriceps', 'Quadriceps'),
    ('hamstrings', 'Hamstrings'),
    ('calves', 'Calves'),
    ('glutes', 'Glutes'),
    ('biceps', 'Biceps'),
    ('triceps', 'Triceps'),
    ('front_deltoid', 'Front Deltoid'),
    ('side_deltoid', 'Side Deltoid'),
    ('rear_deltoid', 'Rear Deltoid'),
    ('core', 'Core'),
    ('forearms', 'Forearms'),
  ]
  
  name = models.CharField(max_length=255)
  description = models.TextField(null=True, blank=True)
  muscles_targeted = models.CharField(max_length=255, null=True, blank=True, choices=muscles_targeted_choices)

  def __str__(self):
    return f"exercise.predefined.{self.name}"

# For custom exercises that users can create
class CustomExercise(models.Model):
  muscles_targeted_choices = [
    ('chest', 'Chest'),
    ('traps', 'Traps'),
    ('rhomboids', 'Rhomboids'),
    ('lats', 'Lats'),
    ('lower_back', 'Lower Back'),
    ('quadriceps', 'Quadriceps'),
    ('hamstrings', 'Hamstrings'),
    ('calves', 'Calves'),
    ('glutes', 'Glutes'),
    ('biceps', 'Biceps'),
    ('triceps', 'Triceps'),
    ('front_deltoid', 'Front Deltoid'),
    ('side_deltoid', 'Side Deltoid'),
    ('rear_deltoid', 'Rear Deltoid'),
    ('core', 'Core'),
    ('forearms', 'Forearms'),
  ]
  
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  description = models.TextField(null=True, blank=True)
  muscles_targeted = models.CharField(max_length=255, null=True, blank=True, choices=muscles_targeted_choices)

  def __str__(self):
    return f"exercise.custom.{self.user.username}.{self.name}"

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
  pinned_notes = models.TextField(null=True, blank=True)

  def __str__(self):
    return f"{self.template.user.username}{self.template.name}.{self.name}"

class SetTemplate(models.Model):
  exercise_template = models.ForeignKey(ExerciseTemplate, on_delete=models.CASCADE)
  set_number = models.IntegerField(null=True, blank=True)
  reps = models.IntegerField(null=True, blank=True)
  weight = models.FloatField(default=0.0, null=True, blank=True)
  rir = models.IntegerField(null=True, blank=True)

  def __str__(self):
    return f"{self.exercise_template.name}.{self.set_number}.w{self.weight}.r{self.reps}"

# For individual set tracking
class Set(models.Model):
  exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="sets")
  set_number = models.IntegerField(null=True, blank=True)
  reps = models.IntegerField(null=True, blank=True)
  weight = models.FloatField(default=0.0, null=True, blank=True)
  rir = models.IntegerField(null=True, blank=True)
  completed_at = models.DateTimeField()

  def __str__(self):
    return f"{self.set_number}.{self.weight}.r{self.reps}"