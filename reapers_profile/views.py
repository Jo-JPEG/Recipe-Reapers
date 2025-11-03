from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from recipe_search.models import Recipe


@login_required  # This decorator handles login protection
def profile_view(request):
    """
    A view to display the user's profile page,
    including their liked recipes.
    """

    user_profile = request.user.profile
    liked_recipes = Recipe.objects.filter(likes__user_profile=user_profile)

    context = {
        'user_profile': user_profile,
        'liked_recipes': liked_recipes,
    }

    return render(request, 'reapers_profile/profile_page.html', context)
