# Generated by Django 5.0.6 on 2024-06-27 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_rename_user_accounts_transfers_user_account_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='transcations',
            new_name='transactions',
        ),
    ]