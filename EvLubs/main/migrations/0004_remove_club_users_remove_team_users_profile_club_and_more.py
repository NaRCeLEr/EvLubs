# Generated by Django 4.2.4 on 2023-09-07 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_profile_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='users',
        ),
        migrations.RemoveField(
            model_name='team',
            name='users',
        ),
        migrations.AddField(
            model_name='profile',
            name='Club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.club'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.team'),
        ),
    ]
