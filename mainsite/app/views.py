from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import utils

@csrf_exempt
def echo(request):
    if request.method == "POST":
        filename = request.POST['file']
        with open(filename) as f:
            output = f.read()
        return(HttpResponse(output))

    return HttpResponse("this endpoint only supports POST requests please try again")


@csrf_exempt
def invert(request):
    if request.method == "POST":
        filename = request.POST['file']
        new_arr = utils.get_2D_array(filename)
        inverted_arr = zip(*new_arr)
        return(HttpResponse(inverted_arr))

        # remember to convert this one to a string
    return HttpResponse("this endpoint only supports POST requests please try again")

#
@csrf_exempt
def flatten(request):
    if request.method == "POST":
        filename = request.POST['file']
        new_arr = utils.get_2D_array(filename)
        output = ','.join(inner for outer in new_arr for inner in outer)
        return(HttpResponse(output))

    return HttpResponse("this endpoint only supports POST requests please try again")
#
@csrf_exempt
def sum(request):
    if request.method == "POST":
        filename = request.POST['file']
        new_arr = utils.get_2D_array(filename)

        total = 0
        for x in new_arr:
            for y in x:
                total += int(y)

        return HttpResponse(total)

    return HttpResponse("this endpoint only supports POST requests please try again")

@csrf_exempt
def multiply(request):
    if request.method == "POST":
        filename = request.POST['file']
        new_arr = utils.get_2D_array(filename)

        total = 1
        for x in new_arr:
            for y in x:
                total *= int(y)

        return HttpResponse(total)

    return HttpResponse("this endpoint only supports POST requests please try again")