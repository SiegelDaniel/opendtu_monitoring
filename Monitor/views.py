import django.http.response
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponseBadRequest, HttpResponse


from Monitor.models import User, Plant
from Monitor.serializers import PlantSerializer, UserSerializer

@csrf_exempt
def userAPI(request, id=0):
    if request.method == 'GET':
        users = User.objects.all()
        user_serializer = UserSerializer(users, many=True)

        return JsonResponse(user_serializer.data, safe=False)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return HttpResponse(200)
        return HttpResponseBadRequest()

    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user = User.objects.get(userId=user_data['userId'])
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return HttpResponse(200)
        return HttpResponseBadRequest()

    elif request.method == 'DELETE':
        user = User.objects.get(userId=id)
        user.delete()