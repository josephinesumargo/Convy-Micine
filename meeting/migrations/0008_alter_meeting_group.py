# Generated by Django 4.0.6 on 2022-07-20 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0007_alter_meeting_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='group',
            field=models.CharField(max_length=225),
        ),
    ]