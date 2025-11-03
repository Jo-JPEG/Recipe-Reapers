from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("recipes/", views.all_recipes, name="all_recipes"),
    path('recipe/<pk>', views.recipe_detail, name="recipe_detail"),
    path('recipe/add/<pk>', views.add_to_favourites, name="add_to_favourites"),
]
