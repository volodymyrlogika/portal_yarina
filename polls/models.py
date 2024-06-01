from django.contrib.auth.models import User
from django.db import models


class Polls(models.Model):
    name = models.CharField(max_length=150, verbose_name="Назва опитування")
    description = models.TextField(verbose_name="Опис опитування")
    question = models.TextField(verbose_name="Питання")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='polls', verbose_name='Автор')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    image = models.ImageField(verbose_name='Картинка', upload_to='polls_images/', blank=True, null=True)
    choice = models.CharField(max_length=30)
