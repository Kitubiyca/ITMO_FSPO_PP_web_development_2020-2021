# Generated by Django 3.1.6 on 2021-04-04 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0010_auto_20210404_2258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='password',
        ),
        migrations.AlterField(
            model_name='owner',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
