from django.contrib.auth.models import User
from django.db import models

class Routine(models.Model):
  """A pre-planned routine that users can reuse to start a workout."""
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=255, null=True, blank=True, default='My New Routine')
  description = models.TextField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.user.username}.{self.name}"

class Exercise(models.Model):
  MUSCLE_GROUP_CHOICES = [
    ('Chest', 'Chest'),
    ('Back', 'Back'),
    ('Legs', 'Legs'),
    ('Shoulders', 'Shoulders'),
    ('Arms', 'Arms'),
    ('Core', 'Core'),
  ]

  """An exercise within a routine or a workout."""
  name = models.CharField(max_length=255, default='New Exercise')
  description = models.TextField(blank=True, null=True)
  muscle_group = models.CharField(max_length=255, blank=True, null=True, choices=MUSCLE_GROUP_CHOICES)
  
  def __str__(self):
    return self.name

class RoutineExercise(models.Model):
  """An exercise that is part of a routine template."""
  routine = models.ForeignKey(Routine, on_delete=models.CASCADE, related_name="routine_exercises")
  exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
  order = models.PositiveIntegerField(default=0)  # Order of exercises in the routine
  description = models.TextField(blank=True, null=True)  # Notes for the exercise
  
  def __str__(self):
    return f"{self.exercise.name} in {self.routine.name}"

class RoutineSet(models.Model):
  """A set template for an exercise within a routine."""
  routine_exercise = models.ForeignKey(RoutineExercise, on_delete=models.CASCADE, related_name="sets")
  reps = models.PositiveIntegerField(default=8)
  weight = models.FloatField(default=0.0)  # Can be bodyweight (0)
  order = models.PositiveIntegerField(default=0)  # Order of sets in the exercise

  def __str__(self):
    return f"{self.reps} reps at {self.weight}lbs in {self.routine_exercise.exercise.name}"

class Workout(models.Model):
  """A live workout session tracked by a user."""
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  routine = models.ForeignKey(Routine, on_delete=models.SET_NULL, null=True, blank=True)
  name = models.CharField(max_length=255, null=True, blank=True, default='My Workout')
  description = models.TextField(blank=True, null=True)
  date = models.DateField(auto_now_add=True, null=True, blank=True)

  def __str__(self):
      return f"Workout by {self.user.username} on {self.started_at}"

class WorkoutExercise(models.Model):
  """An exercise performed during a live workout session."""
  workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="workout_exercises")
  exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
  order = models.PositiveIntegerField(default=0)

  def __str__(self):
      return f"{self.exercise.name} in workout {self.workout.id}"

class WorkoutSet(models.Model):
  """A set tracked within a live workout session."""
  workout_exercise = models.ForeignKey(WorkoutExercise, on_delete=models.CASCADE, related_name="sets")
  reps = models.PositiveIntegerField(default=8)
  weight = models.FloatField(default=0.0)  # 0 = bodyweight
  completed = models.BooleanField(default=False)  # Mark if the set was completed
  order = models.PositiveIntegerField(default=0)

  def __str__(self):
      return f"{self.reps} reps at {self.weight}lbs in {self.workout_exercise.exercise.name}"