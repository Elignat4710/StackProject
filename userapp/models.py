from django.db import models
from django.contrib.auth.models import User, AbstractUser
# from questionsapp.models import Tag


class MyUser(AbstractUser):

    ACTIVITY = [
        ('I', 'Institute'),
        ('W', 'Work')
    ]

    date_of_birth = models.DateField(
        verbose_name='date of birth',
        blank=True,
        null=True
    )
    rating = models.IntegerField(
        verbose_name='rating',
        default=10,
    )
    activity_type = models.CharField(
        choices=ACTIVITY,
        max_length=10,
        blank=True
    )
    activity_place = models.TextField(
        verbose_name='activity place',
        blank=True
    )
    skills = models.ManyToManyField(
        'questionsapp.Tag',
         blank=True,
         related_name='users'
         )
    avatar = models.ImageField(
        verbose_name='avatar',
        upload_to='accounts/avatar/%Y/%m/',
        blank=True
    )
