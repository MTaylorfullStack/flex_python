from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("You have handled your first web request!")

def new(request):
    return HttpResponse("You have just sent ANOTHER request")