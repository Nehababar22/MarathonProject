# Generated by Django 4.0 on 2021-12-26 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Marathon_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(auto_now_add=True),
        ),
    ]
