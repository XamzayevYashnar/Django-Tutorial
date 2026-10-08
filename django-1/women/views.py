from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

# Представление

def index(request):
    return HttpResponse("Страница приложение Women")