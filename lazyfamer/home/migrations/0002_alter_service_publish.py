# Generated by Django 4.0.6 on 2022-07-16 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='publish',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
