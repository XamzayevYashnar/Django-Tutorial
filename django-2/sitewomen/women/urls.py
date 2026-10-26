from django.urls import path, re_path, register_converter
from . import views
from .convertors import FourDigitYearConvertor, NameConvertor

register_converter(FourDigitYearConvertor, "year4")
register_converter(NameConvertor, "name5")

urlpatterns = [
    path('', views.index),  # http://127.0.0.1:8000
    path('cats/<int:cat_id>/', views.categories), # http://127.0.0.1:8000/cats/2/
    path('cats/<slug:cat_slug>/', views.categories_by_slug), # http://127.0.0.1:8000/cats/some/
    re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive),
    path('archive/<year4:year>/', views.archive),
    path('name/<name5:name>/', views.name),
]
