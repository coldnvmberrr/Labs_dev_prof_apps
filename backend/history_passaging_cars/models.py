from django.db import models


class HistoryPassagingCars(models.Model):
    datetime = models.DateTimeField(verbose_name='Дата и время')
    number = models.CharField(verbose_name='Номерной знак')
    model = models.CharField(verbose_name='Марка автомобиля')

    class Meta:
        verbose_name = 'Запись проезда автомобили'
        verbose_name_plural = 'История проезжающих автомобилей'
        unique_together = ('datetime', 'number', 'model')