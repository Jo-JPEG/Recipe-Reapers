from django.db.models import Q
from django.shortcuts import render, redirect

from .models import Recipe
from reapers_profile.models import UserLike


def index(request):
    """
    View to return to the index page with search results and highlights.
    """

    relevant_recipes = None
    search_query = ""

    if request.method == "POST":
        search_query = request.POST.get("q", "").strip()
        if search_query:
            relevant_recipes = Recipe.objects.filter(
                Q(title__icontains=search_query) | Q(
                    recipe__icontains=search_query)
            ).order_by("title")
        else:
            relevant_recipes = Recipe.objects.none()

    context = {
        "relevant_recipes": relevant_recipes,
        "search_query": search_query,
    }

    return render(request, "recipe_search/index.html", context)


def all_recipes(request):
    """Render the All Recipes catalog with optional search filtering."""

    search_query = request.GET.get("q", "").strip()

    recipes_qs = Recipe.objects.all()
    if search_query:
        recipes_qs = recipes_qs.filter(
            Q(title__icontains=search_query) | Q(
                    recipe__icontains=search_query)
        )

    recipes = list(recipes_qs.order_by("title"))

    fright_meter_patterns = [35, 45, 55, 65]
    recipe_cards = []
    for index, recipe in enumerate(recipes):
        trick_percent = fright_meter_patterns[index % len(
            fright_meter_patterns)]
        treat_percent = max(0, 100 - trick_percent)
        pointer_percent = max(4, min(96, trick_percent))
        recipe_cards.append(
            {
                "recipe": recipe,
                "trick_percent": trick_percent,
                "treat_percent": treat_percent,
                "pointer_percent": pointer_percent,
            }
        )

    context = {
        "search_query": search_query,
        "recipe_cards": recipe_cards,
        "results_count": len(recipe_cards),
    }

    return render(request, "recipe_search/all_recipes.html", context)


def recipe_detail(request, pk):
    """Displays full recipe"""

    recipe = Recipe.objects.get(pk=pk)
    print("This is the recipe: ", recipe.title)

    context = {'recipe': recipe}

    return render(request, "recipe_search/recipe_detail.html", context)


def add_to_favourites(request, pk):
    """gets user credantials, creates instance of user like for recipe"""

    user_profile = request.user.profile
    recipe = Recipe.objects.get(pk=pk)

    user_like, created = UserLike.objects.get_or_create(
        user_profile=user_profile,
        recipe=recipe
    )

    return redirect('profile')
