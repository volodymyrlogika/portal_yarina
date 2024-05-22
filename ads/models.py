from django.contrib.auth.models import User
from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст оголошення')
    image = models.ImageField(verbose_name='Картинка', upload_to='ads_images/',blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads', verbose_name='Автор')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
