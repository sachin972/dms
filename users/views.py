from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def index(req):
    return JsonResponse({'message': "Run successfully"})