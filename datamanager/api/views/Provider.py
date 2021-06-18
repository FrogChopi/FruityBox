from api.models import Provider
from api.serializers import ProviderSerializer
from django.http import JsonResponse

def get (request) :
    f = Provider.objects.all()
    s = ProviderSerializer(f, many=True)
    return JsonResponse(s.data, safe=False)

def provider(request) :
    methods = {
        'GET' : get
    }

    if methods[request.method] :
        return methods[request.method](request)
    else :
        return JsonResponse('', status = 400)