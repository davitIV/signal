from subprocess import Popen
from django.shortcuts import render
from django.http import JsonResponse
from .models import User


def fetch_users(request):
    users = User.objects.all().values('name', 'email')
    return JsonResponse(list(users), safe=False)


def index(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        users = User.objects.all().values('name', 'email')
        return JsonResponse(list(users), safe=False)
    else:
        return render(request, 'index.html')