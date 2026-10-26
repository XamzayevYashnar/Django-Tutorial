from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

# Представление

def index(request):
    return HttpResponse("Страница приложение Women")

def categories(request, cat_slug):
    return HttpResponse(f"Страница: {cat_slug}")