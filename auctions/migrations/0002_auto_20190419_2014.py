# Generated by Django 2.1.7 on 2019-04-19 20:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auctions', '0001_initial'),
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='attorney',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Attorney'),
        ),
        migrations.AddField(
            model_name='bid',
            name='bidder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bidder', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bid',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bid',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Client'),
        ),
        migrations.AddField(
            model_name='bid',
            name='previousBid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.Bid'),
        ),
    ]
