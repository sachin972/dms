from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def SignUP(req):
    return JsonResponse({'message': "Run successfully"})

def SignIN(req, res):
    return HttpResponse("Success")


def UpdateRole(req, res):
    return HttpResponse("Role Updated")