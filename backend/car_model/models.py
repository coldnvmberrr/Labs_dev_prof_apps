from django.db import models


class CarModel(models.Model):
    name = models.CharField(verbose_name='Название марки', unique=True)

    class Meta:
        verbose_name = 'Марка автомобиля'
        verbose_name_plural = 'Марки автомобилей'
