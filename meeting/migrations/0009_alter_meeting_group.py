# Generated by Django 4.0.6 on 2022-07-20 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0006_announcement_body'),
        ('meeting', '0008_alter_meeting_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='group.group'),
        ),
    ]