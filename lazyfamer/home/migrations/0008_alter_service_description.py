# Generated by Django 4.0.6 on 2022-07-17 12:04

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_service_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='description',
            field=ckeditor.fields.RichTextField(blank='True', null=True),
        ),
    ]
