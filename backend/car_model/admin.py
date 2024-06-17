from django.contrib import admin

from car_model.models import CarModel


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    """Вывод данных в админку"""
    list_display = ('id', 'name',)
    search_fields = ()
