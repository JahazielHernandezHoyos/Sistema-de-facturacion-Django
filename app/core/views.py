from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
def myfirstview(request):
    data = {
        'name': 'Juan',
    }
    return JsonResponse(data)

