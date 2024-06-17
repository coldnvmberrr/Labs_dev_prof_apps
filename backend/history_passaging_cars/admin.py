from django.contrib import admin

from history_passaging_cars.models import HistoryPassagingCars


@admin.register(HistoryPassagingCars)
class HistoryPassagingCarsAdmin(admin.ModelAdmin):
    """Вывод данных в админку"""
    list_display = ('id', 'datetime',)
    # list_display_links = ('id', 'datetime', 'car__model', 'car__number' )
    search_fields = ()
