from django.db import models
from stackproj import settings


class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.title)


class Question(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    body = models.TextField(
        verbose_name='body of question'
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    tags = models.ManyToManyField(
        'Tag',
        blank=True,
        related_name='questions'
    )
    title = models.CharField(max_length=200)
    answers = models.ManyToManyField(
        'Answer',
        blank=True,
        related_name='answers'
    )

    def __str__(self):
        return self.title


class Answer(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    body = models.TextField(
        verbose_name='body of answer'
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.body