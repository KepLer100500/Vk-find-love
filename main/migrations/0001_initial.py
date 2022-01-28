# Generated by Django 3.1.7 on 2021-11-22 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия')),
                ('sex', models.CharField(blank=True, max_length=30, null=True, verbose_name='Пол')),
                ('bdate', models.CharField(blank=True, max_length=30, null=True, verbose_name='Дата рождения')),
                ('city', models.CharField(blank=True, max_length=255, null=True, verbose_name='Город')),
                ('country', models.CharField(blank=True, max_length=255, null=True, verbose_name='Страна')),
                ('photo_200', models.URLField(blank=True, null=True, verbose_name='Ссылка на фото')),
            ],
            options={
                'verbose_name': 'Кандидат',
                'verbose_name_plural': 'Кандидаты',
            },
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_work_now', models.BooleanField(verbose_name='Сейчас в работе')),
                ('user_searcher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Поиск',
                'verbose_name_plural': 'Поиски',
            },
        ),
        migrations.CreateModel(
            name='CandidateGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=255, verbose_name='Название группы')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.candidate', verbose_name='ID Кандидата')),
            ],
            options={
                'verbose_name': 'Группа кандидата',
                'verbose_name_plural': 'Группы кандидатов',
            },
        ),
        migrations.AddField(
            model_name='candidate',
            name='search',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.search', verbose_name='ID попытки поиска'),
        ),
    ]
