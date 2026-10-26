from django.urls import path
from women.views import index, categories

urlpatterns = [
    path("", index, name="womens"),
    path("categories/<slug:cat_slug>/", categories, name="categories"),
]