from django.db import models
from django.contrib.auth.models import User
from recipe_search.models import Recipe  # Import your Recipe model

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    # This is the field for "liked recipes"
    liked_recipes = models.ManyToManyField(
        Recipe, 
        related_name='liked_by', 
        blank=True
    )

    def __str__(self):
        return self.user.username
