# Generated by Django 3.0.6 on 2020-06-03 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_auto_20200603_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodintake',
            name='food_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Food'),
        ),
    ]
