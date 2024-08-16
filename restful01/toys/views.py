from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from django.http import JsonResponse  # Corrigido para JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Toy
from .serializers import ToySerializer

# Create your views here.
#def home(request):
#    return HttpResponse("Olá mundo!")

@csrf_exempt
def toy_list(request):
    if request.method == 'GET':
        toys = Toy.objects.all()
        toys_serializer = ToySerializer(toys, many=True)
        return JsonResponse(toys_serializer.data)
    elif request.method == 'POST':
        toy_data = JSONParser().parse(request)
        toy_serializer = ToySerializer(data=toy_data)
        if toy_serializer.is_valid():
            toy_serializer.save()
            return JsonResponse(toy_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(toy_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@csrf_exempt
def toy_detail(request, pk):
    try:
        toy = Toy.objects.get(pk=pk)
    except Toy.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        toy_serializer = ToySerializer(toy)
        return JsonResponse(toy_serializer.data)
    elif request.method == 'DELETE':
        toy.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)