from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from car_model.models import CarModel
from history_passaging_cars.models import HistoryPassagingCars


def history(request):
    items = HistoryPassagingCars.objects.all().order_by('id')
    return render(request, 'index.html', {'items': items})


@csrf_exempt
def add(request):
    models = CarModel.objects.all()
    if request.method == 'POST':
        data = request.POST
        HistoryPassagingCars.objects.create(
            model_id=data.get('model', models.first().id),
            number=data['number'],
            datetime=data['datetime']
        )
        return HttpResponseRedirect("/")
    else:
        return render(request, 'add.html', {'models': models})
