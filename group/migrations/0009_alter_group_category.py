# Generated by Django 4.0.6 on 2022-07-21 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0008_alter_group_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='category',
            field=models.CharField(choices=[('PERSONAL', 'PERSONAL'), ('CCA', 'CCA'), ('MODULE', 'MODULE'), ('PROJECT', 'PROJECT')], default='PERS', max_length=10),
        ),
    ]
