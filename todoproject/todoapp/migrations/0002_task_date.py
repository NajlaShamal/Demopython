# Generated by Django 4.2.9 on 2024-01-11 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1997-02-04'),
            preserve_default=False,
        ),
    ]