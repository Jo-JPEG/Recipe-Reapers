from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(
        'auth.User', on_delete=models.CASCADE, related_name='profile'
    )
    user_recipes = models.ManyToManyField(
        'recipe_search.Recipe', blank=True, related_name='profiles'
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"