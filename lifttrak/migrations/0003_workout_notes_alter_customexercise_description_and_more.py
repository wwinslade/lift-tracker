# Generated by Django 5.1.6 on 2025-02-07 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lifttrak", "0002_set_rir_settemplate"),
    ]

    operations = [
        migrations.AddField(
            model_name="workout",
            name="notes",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="customexercise",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="customexercise",
            name="muscles_targeted",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="exercisetemplate",
            name="pinned_notes",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="predefinedexercise",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="predefinedexercise",
            name="muscles_targeted",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="set",
            name="completed_at",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="set",
            name="reps",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="set",
            name="rir",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="set",
            name="set_number",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="set",
            name="weight",
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name="settemplate",
            name="reps",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="settemplate",
            name="rir",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="settemplate",
            name="set_number",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="settemplate",
            name="weight",
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name="workouttemplate",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
