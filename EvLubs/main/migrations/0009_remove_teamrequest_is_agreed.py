# Generated by Django 4.2.4 on 2023-10-12 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_teamrequest_is_checked_alter_teamrequest_is_agreed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamrequest',
            name='is_agreed',
        ),
    ]
