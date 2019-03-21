# Generated by Django 2.1.7 on 2019-03-19 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(error_messages={'blank': 'Email Field cannot be blank', 'invalid': 'Must choose a valid email', 'invalid_choice': 'Invalid email choice', 'null': 'Email must not be null', 'unique': 'Please choose a unique email'}, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(error_messages={'blank': 'Password Field cannot be blank', 'invalid': 'Must choose a valid password', 'invalid_choice': 'Invalid password choice', 'null': 'Password must not be null', 'unique': 'Please choose a unique password'}, max_length=500, unique=True),
        ),
    ]