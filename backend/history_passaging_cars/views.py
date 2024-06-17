from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from history_passaging_cars.models import HistoryPassagingCars


def history(request):
    items = HistoryPassagingCars.objects.all().order_by('id')
    return render(request, 'index.html', {'items': items})


@csrf_exempt
def add(request):
    if request.method == 'POST':
        data = request.POST
        HistoryPassagingCars.objects.create(
            model=data['model'],
            number=data['number'],
            datetime=data['datetime']
        )
        return HttpResponseRedirect("/")
    else:
        return render(request, 'add.html')
