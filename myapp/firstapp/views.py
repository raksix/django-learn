from django.shortcuts import render
from django.http import JsonResponse
from . import mongo
import json
import datetime

# Create your views here.
def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == "POST":
        body = json.loads(request.body)

        if not body["username"] or not body["password"] or not body["email"]:
            return JsonResponse(
                {
                    "error": True,
                    "message": "Please provide all the required fields",
                }
            )
        
        exists_user = mongo.users.find_one({
            "$or": [
                {"username": body["username"]},
                {"email": body["email"]}
            ]
        })

        if exists_user:
            return JsonResponse(
                {
                    "error": True,
                    "message": "User already exists",
                }
            )
            

        mongo.users.insert_one({
            "username": body["username"],
            "password": body["password"],
            "email": body["email"],
            "data": datetime.datetime.now()
        })

        return JsonResponse(
            {
                "error": False,
                "message": "User registered successfully",
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
    return JsonResponse(
        {
            "duyurular": [
                {"head": "Duyuru 1", "content": "Duyuru 1 içeriği"},
                {"head": "Duyuru 2", "content": "Duyuru 2 içeriği"},
            ]
        }
    )
