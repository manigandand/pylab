from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.


def index(request):
    return HttpResponse("Poll app")


def json_test_handler(request):
    return JsonResponse({
            'key1': 'value1',
            'key2': [
                {
                    'key2.1': 'val1',
                },
            ],
            })