from django.db import models

from car_model.models import CarModel


class HistoryPassagingCars(models.Model):
    datetime = models.DateTimeField(verbose_name='Дата и время')
    number = models.CharField(verbose_name='Номерной знак')
    model = models.ForeignKey(CarModel, verbose_name='Марка', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Запись проезда автомобили'
        verbose_name_plural = 'История проезжающих автомобилей'
        unique_together = ('datetime', 'number', 'model')
