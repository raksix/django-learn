from django.shortcuts import render
from django.http import JsonResponse
from . import mongo


# Create your views here.
def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == "POST":
        return JsonResponse(
            {
                "error": False,
                "message": "Only POST method is allowed for this endpoint",
            }
        )
    else:
        return JsonResponse(
            {
                "error": True,
                "message": "Only POST method is allowed for this endpoint",
            }
        )


def duyurular(request):

    print(request.method)

    return JsonResponse(
        {
            "duyurular": [
                {"head": "Duyuru 1", "content": "Duyuru 1 içeriği"},
                {"head": "Duyuru 2", "content": "Duyuru 2 içeriği"},
            ]
        }
    )
