# Generated by Django 3.0.6 on 2020-06-03 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0024_auto_20200603_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='foodintake',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
