from django.http import HttpResponse
from django.shortcuts import render


def index(request): # HttpRequest
    return HttpResponse("Страница приложения women.")


def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}</p>")

def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_slug}</p>")

def archive(request, year):
    return HttpResponse(f"<h1>Archive from years: <p>{year}</p></h1>")

def name(request, name):
    return HttpResponse(f"<h1>Name: <p>{name}</p></h1>")