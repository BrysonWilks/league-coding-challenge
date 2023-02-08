from django.http import HttpResponse
from . import utils

def echo(request):
    if request.method == "POST":
        try:
            filename = request.POST['file']
            with open(filename) as f:
                output = f.read()
            return(HttpResponse(output))
        except:
            return(HttpResponse("Could not parse file, please make sure it's in csv format"))

    return HttpResponse("this endpoint only supports POST requests please try again")


def invert(request):
    if request.method == "POST":
        try:
            filename = request.POST['file']
            new_arr = utils.get_2D_array(filename)
            inverted_arr = zip(*new_arr)

            output = ""
            for i in inverted_arr:
                output += (','.join(map(str, i)))
                output += "\n"
            return (HttpResponse(output))
        except:
            return(HttpResponse("Could not parse file, please make sure it's in csv format"))

    return HttpResponse("this endpoint only supports POST requests please try again")

#
def flatten(request):
    if request.method == "POST":
        try:
            filename = request.POST['file']
            new_arr = utils.get_2D_array(filename)
            output = ','.join(inner for outer in new_arr for inner in outer)
            return(HttpResponse(output))
        except:
            return (HttpResponse("Could not parse file, please make sure it's in csv format"))

    return HttpResponse("this endpoint only supports POST requests please try again")
#

def sum(request):
    if request.method == "POST":
        try:
            filename = request.POST['file']
            new_arr = utils.get_2D_array(filename)

            total = 0

            for x in new_arr:
                for y in x:
                    if y.isnumeric():
                        total += int(y)

            return HttpResponse(total)
        except:
            return HttpResponse("Could not parse file, please make sure it's in csv format")

    return HttpResponse("this endpoint only supports POST requests please try again")

def multiply(request):
    if request.method == "POST":
        try:
            filename = request.POST['file']
            new_arr = utils.get_2D_array(filename)

            total = 1

            for x in new_arr:
                for y in x:
                    if y.isnumeric():
                        total *= int(y)

            return HttpResponse(total)
        except:
            return HttpResponse("Could not parse file, please make sure it's in csv format")

    return HttpResponse("this endpoint only supports POST requests please try again")


def home(request):
    err_message = "Whoops! Looks like you forgot your endpoint. \n\nThe correct choices are 'sum', 'multiply', 'echo', 'invert', and 'flatten'"
    return HttpResponse(err_message)