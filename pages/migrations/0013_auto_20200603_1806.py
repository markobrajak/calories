# Generated by Django 3.0.6 on 2020-06-03 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_auto_20200603_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]