from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    image = models.ImageField(verbose_name='Картинка', upload_to='portfolio_images/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='portfolio', verbose_name='Автор')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    file = models.FileField(upload_to='portfolio_files/', verbose_name='Файли')

    def __str__(self):
        return self.title