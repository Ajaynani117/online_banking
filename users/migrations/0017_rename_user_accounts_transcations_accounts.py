# Generated by Django 5.0.6 on 2024-06-26 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_rename_user_accounts_id_transcations_user_accounts_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transcations',
            old_name='user_accounts',
            new_name='accounts',
        ),
    ]