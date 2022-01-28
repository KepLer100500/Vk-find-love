from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Search(models.Model):
    user_searcher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    in_work_now = models.BooleanField(verbose_name='Сейчас в работе')

    def __str__(self):
        return f'{self.user_searcher}, In work: {self.in_work_now}'

    class Meta:
        verbose_name_plural = 'Поиски'
        verbose_name = 'Поиск'


class Candidate(models.Model):
    search = models.ForeignKey(Search, on_delete=models.CASCADE, verbose_name='ID попытки поиска')
    first_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Фамилия')
    vkid = models.CharField(max_length=30, null=True, blank=True, verbose_name='vkid')
    bdate = models.CharField(max_length=30, null=True, blank=True, verbose_name='Дата рождения')
    city = models.CharField(max_length=255, null=True, blank=True, verbose_name='Город')
    country = models.CharField(max_length=255, null=True, blank=True, verbose_name='Страна')
    photo_200 = models.URLField(null=True, blank=True, verbose_name='Ссылка на фото')

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.bdate}, {self.vkid}, {self.city})'

    class Meta:
        verbose_name_plural = 'Кандидаты'
        verbose_name = 'Кандидат'


class CandidateGroups(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, verbose_name='ID Кандидата')
    group_name = models.CharField(max_length=255, verbose_name='Название группы')

    def __str__(self):
        return f'{self.group_name} - {self.candidate}'

    class Meta:
        verbose_name_plural = 'Группы кандидатов'
        verbose_name = 'Группа кандидата'
