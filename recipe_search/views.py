from django.shortcuts import render


def index(request):
    """
    View to return to the index page
    """

    return render(request, "recipe_search/index.html")


def all_recipes(request):
    """
    Temporary simple view to render the All Recipes template without data.
    """

    return render(request, "recipe_search/all_recipes.html")
