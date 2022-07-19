# Generated by Django 4.0.6 on 2022-07-19 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0002_alter_meeting_managers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meeting',
            options={'ordering': ('-start_time',)},
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='dates',
        ),
        migrations.AlterField(
            model_name='meeting',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
