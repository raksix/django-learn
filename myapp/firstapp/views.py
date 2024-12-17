from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request, "index.html")


def duyurular(request):
    return JsonResponse({
        "duyurular": [
            {"head": "Duyuru 1", "content": "Duyuru 1 içeriği"},
            {"head": "Duyuru 2", "content": "Duyuru 2 içeriği"},
        ]
    })
