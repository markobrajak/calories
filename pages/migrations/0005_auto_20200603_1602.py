# Generated by Django 3.0.6 on 2020-06-03 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20200602_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodintake',
            name='food_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Food'),
        ),
    ]
