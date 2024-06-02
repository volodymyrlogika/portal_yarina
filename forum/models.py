from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    title = models.CharField(max_length=200, verbose_name='Тема')
    description = models.TextField(verbose_name='Опис')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics', verbose_name='Автор')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Створено')

    def __str__(self):
        return self.title

class Message(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='message', verbose_name='Тема')
    text = models.TextField(verbose_name='Опис')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages', verbose_name='Автор')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Створено')

    def __str__(self):
        return self.text