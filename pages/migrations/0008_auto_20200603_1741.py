# Generated by Django 3.0.6 on 2020-06-03 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20200603_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodintake',
            name='food_id',
            field=models.IntegerField(),
        ),
    ]
