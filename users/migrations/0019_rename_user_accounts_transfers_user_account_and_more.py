# Generated by Django 5.0.6 on 2024-06-26 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_rename_accounts_transcations_account'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transfers',
            old_name='user_accounts',
            new_name='user_account',
        ),
        migrations.RenameField(
            model_name='user_accounts',
            old_name='accounts_no',
            new_name='account_no',
        ),
        migrations.RenameField(
            model_name='user_accounts',
            old_name='accounts_type',
            new_name='accounttype',
        ),
    ]
