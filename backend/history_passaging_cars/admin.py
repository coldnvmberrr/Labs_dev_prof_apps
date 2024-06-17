from django.contrib import admin

from history_passaging_cars.models import HistoryPassagingCars


@admin.register(HistoryPassagingCars)
class HistoryPassagingCarsAdmin(admin.ModelAdmin):
    """Вывод данных в админку"""
    list_display = ('id', 'datetime',)
    search_fields = ()
