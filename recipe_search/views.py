from django.shortcuts import render
from django.db.models import Q

from .models import Recipe


def index(request):
    """
    View to return to the index page
    """

    if request.method == "GET":
        return render(request, "recipe_search/index.html")

    else:
        query = request.GET.get("query", "")

        relevant_recipes = Recipe.objects.filter(
            Q(title__icontains=query) | Q(recipe__icontains=query)
        )

        context = {
            'relevent_recipes': relevant_recipes,
        }

        return render(
            request,
            "recipe_search/index.html",
            context,
        )
