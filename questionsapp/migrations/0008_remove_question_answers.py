# Generated by Django 3.0.3 on 2020-03-04 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionsapp', '0007_auto_20200304_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answers',
        ),
    ]
