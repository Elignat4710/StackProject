from django.db import models
from stackproj import settings


class Tag(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(
        verbose_name='description'
    )

    def __str__(self):
        return '{}'.format(self.title)


class StampedModel(models.Model):
    created_on = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        abstract = True


class Question(StampedModel):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    
    body = models.TextField(
        verbose_name='body of question'
    )
    tags = models.ManyToManyField(
        'Tag',
        blank=True,
        related_name='questions'
    )
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
 

class Answer(StampedModel):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    body = models.TextField(
        verbose_name='body of answer'
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers'
    )

    def __str__(self):
        return self.body