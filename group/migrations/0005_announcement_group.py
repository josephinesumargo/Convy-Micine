# Generated by Django 4.0.6 on 2022-07-19 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0004_remove_announcement_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='group.group'),
        ),
    ]
