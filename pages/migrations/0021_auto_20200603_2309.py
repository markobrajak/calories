# Generated by Django 3.0.6 on 2020-06-03 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0020_auto_20200603_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodintake',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
