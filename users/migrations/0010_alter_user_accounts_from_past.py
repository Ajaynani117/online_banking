# Generated by Django 5.0.6 on 2024-06-25 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_user_recipients_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_accounts',
            name='From_past',
            field=models.TextField(blank=True),
        ),
    ]
