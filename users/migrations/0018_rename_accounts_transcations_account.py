# Generated by Django 5.0.6 on 2024-06-26 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_rename_user_accounts_transcations_accounts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transcations',
            old_name='accounts',
            new_name='account',
        ),
    ]