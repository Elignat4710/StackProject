# Generated by Django 3.0.3 on 2020-03-04 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_auto_20200304_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='activity_type',
            field=models.CharField(blank=True, choices=[('I', 'Institute'), ('W', 'Work')], max_length=10),
        ),
    ]
