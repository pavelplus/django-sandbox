from django.db import models


class Person(models.Model):
    SEX_CHOICES = {
        'm': 'мужской',
        'f': 'женский',
    }
    
    name = models.CharField(max_length=50, db_index=True, verbose_name='имя')
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, verbose_name='пол')
    birth_date = models.DateField(null=True, blank=True, verbose_name='дата рождения')
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True, verbose_name='телефон')
    notes = models.TextField(blank=True, verbose_name='заметки')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='изменен')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'персона'
        verbose_name_plural = 'персоны'
        ordering = ['name']
