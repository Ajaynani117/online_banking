# Generated by Django 5.0.6 on 2024-07-23 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_alter_user_email_id_alter_user_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='zipcode',
            field=models.IntegerField(max_length=100),
        ),
    ]