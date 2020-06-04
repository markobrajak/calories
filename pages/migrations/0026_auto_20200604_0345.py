# Generated by Django 3.0.6 on 2020-06-04 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0025_auto_20200604_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caloriesburnedtraining',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='caloriesburnedtraining',
            name='training_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Training'),
        ),
        migrations.AlterField(
            model_name='training',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]