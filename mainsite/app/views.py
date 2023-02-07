from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import csv

# Create your views here


@csrf_exempt
def echo(request):
    if request.method == "POST":
        print("200 POST REQUEST RECEIVED")

    return HttpResponse("ECHO REQUEST RECEIVED")


@csrf_exempt
def invert(request):
    pass

#
@csrf_exempt
def flatten(request):
    pass
#
@csrf_exempt
def sum(request):
    pass

@csrf_exempt
def multiply(request):
    pass