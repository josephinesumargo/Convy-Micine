# Generated by Django 4.0.6 on 2022-07-20 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0005_announcement_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='body',
            field=models.TextField(blank=True),
        ),
    ]
