from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import csv

# Create your views here


@csrf_exempt
def echo(request):
    if request.method == "POST":
        filename = request.POST['file']
        f = open(filename, "r")
        #print(f.read())
        return(HttpResponse(f))

    return HttpResponse("this endpoint only supports POST requests please try again")


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