from django.shortcuts import render


def reaper_profile(request):
    """View to display a users profile"""

    return render(request, 'reapers_profile/profile.html')
