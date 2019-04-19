# Generated by Django 2.1.7 on 2019-04-19 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caseType1', models.CharField(max_length=250)),
                ('caseType2', models.CharField(max_length=250)),
                ('caseType3', models.CharField(max_length=250)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CaseAdmin',
            fields=[
                ('case_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cases.Case')),
            ],
            bases=('cases.case',),
        ),
    ]
