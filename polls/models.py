from django.contrib.auth.models import User
from django.db import models


class Poll(models.Model):
    name = models.CharField(max_length=150, verbose_name="Назва опитування")
    description = models.TextField(verbose_name="Опис опитування")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='polls', verbose_name='Автор')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Створено')

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.CharField(max_length=500, verbose_name="Запитання")
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='questions', verbose_name='Запитання')
    points = models.IntegerField(default=1, verbose_name='Кількість балів')
    image = models.ImageField(verbose_name='Картинка', upload_to='polls_images/', blank=True, null=True)

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.CharField(max_length=500, verbose_name="Варіант відповіді")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers', verbose_name='Запитання')
    is_correct = models.BooleanField(verbose_name='Правильна відповідь')

    def __str__(self):
        return self.text


class PollResult(models.Model):
    completed_by = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='completed_polls', verbose_name='Респондент')
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='results', verbose_name='Результати')
    completed_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата і час проходження')
    score = models.IntegerField(null=True, blank=True, verbose_name='Оцінка')

    def __str__(self):
        return f'{self.completed_by} - {self.poll} - {self.score}'