# Generated by Django 3.0.6 on 2020-06-03 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_auto_20200603_2243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foodintake',
            old_name='food_id_a',
            new_name='food_id',
        ),
    ]
