# Generated by Django 5.0.6 on 2024-06-24 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_transcations_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_transcations',
            name='amount',
            field=models.FloatField(default=None),
        ),
    ]