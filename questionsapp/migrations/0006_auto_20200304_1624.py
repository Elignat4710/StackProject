# Generated by Django 3.0.3 on 2020-03-04 16:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('questionsapp', '0005_answer_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]