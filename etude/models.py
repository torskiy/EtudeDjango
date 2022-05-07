from django.db import models
from django.urls import reverse

# Create your models here.


class Case(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=150, verbose_name='URL')
    description = models.CharField(max_length=255, blank=True, verbose_name='Описание кейса')
    title_image = models.ImageField(upload_to='cases/', verbose_name='Фото превью')
    video = models.URLField(blank=True, verbose_name='Ссылка на видео')
    content = models.TextField(blank=True, verbose_name='Задача и решение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_case', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Кейс'
        verbose_name_plural = 'Кейсы'
        ordering = ['-created_at']


class CasePhoto(models.Model):
    photo = models.ImageField(upload_to='CasePhotos/%Y/%m/%d/', verbose_name='Фото')
    case = models.ForeignKey('Case', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Бэкстейдж фото(in developing)'
        verbose_name_plural = 'Бэкстейдж фото(in developing)'


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    second_name = models.CharField(max_length=100, blank=True, verbose_name='Фамилия')
    position = models.CharField(max_length=100, blank=True, verbose_name='Должность')
    photo = models.ImageField(blank=True, upload_to='contacts/', verbose_name='Фото')
    tel = models.CharField(max_length=20, verbose_name='Телефон')
    e_mail = models.EmailField(verbose_name='E-Mail')
    instagram = models.URLField(blank=True, verbose_name='Instagram')
    telegram = models.URLField(blank=True, verbose_name='Telegram')
    vk = models.URLField(blank=True, verbose_name='VK')
    youtube = models.URLField(blank=True, verbose_name='YouTube')
    main_contact = models.BooleanField(default=False, verbose_name='Основной контакт')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class StaticData(models.Model):
    showreel = models.FileField(upload_to='static_files/showreel/', verbose_name='Шоурил')
    home = models.TextField(blank=True, verbose_name='Главная')
    about = models.TextField(blank=True, verbose_name='О нас')
    contact_us = models.TextField(blank=True, verbose_name='Cвязаться с нами')
    documents = models.FileField(blank=True, upload_to='documents/', verbose_name='Документы')
    briefing = models.URLField(blank=True, verbose_name='Брифинг')
    main = models.BooleanField(default=False, verbose_name='Main Static Data')

    class Meta:
        verbose_name_plural = 'StaticData'
