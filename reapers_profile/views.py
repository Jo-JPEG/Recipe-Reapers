from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserProfile # Make sure to import your UserProfile

@login_required  # This decorator handles login protection
def profile_view(request):
    """
    A view to display the user's profile page,
    including their liked recipes.
    """
    
    # We get the user from the 'request' object
    # We can get the profile via the 'related_name'
    # we set on the OneToOneField (user.profile)
    try:
        profile = request.user.profile
        # Get all recipes from the ManyToManyField
        liked_recipes = profile.liked_recipes.all()
    except UserProfile.DoesNotExist:
        # A fallback in case a profile wasn't automatically created
        # for a user (e.g., if you're using signals and one failed)
        profile = None
        liked_recipes = []

    context = {
        'profile': profile,
        'user': request.user,
        'liked_recipes': liked_recipes
    }
    
    return render(request, 'reapers_profile/profile_page.html', context)
