from api.models import Fruit
from api.serializers import FruitSerializer
from django.http import JsonResponse

def get (request) :
    f = Fruit.objects.all()
    s = FruitSerializer(f, many=True)
    return JsonResponse(s.data, safe=False)

def fruit(request) :
    methods = {
        'GET' : get
    }

    if methods[request.method] :
        return methods[request.method](request)
    else :
        return JsonResponse('', status = 400)