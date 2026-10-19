from django.shortcuts import HttpResponse

def portail(request):
    return HttpResponse(
        "Welcome to the Accumulator Portal!"
    )