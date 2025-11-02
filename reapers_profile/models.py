from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from recipe_search.models import Recipe


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile'
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"


class UserLike(models.Model):
    """Instances of each time a user likes a recipe"""

    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="likes"
    )

    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="likes"
    )

    class Meta:
        unique_together = ("user_profile", "recipe")


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """

    if created:
        # Create the profile when the user is first created
        user_profile = UserProfile.objects.create(user=instance)
    else:
        # Existing user: update the user profile
        user_profile = instance.profile

    # Save the profile in case of any changes
    user_profile.save()
