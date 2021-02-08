from django.shortcuts import render
from .models import *


def home(request):
    context={
        'all_users': User.objects.all()
    }
    return render(request, "home.html", context)
