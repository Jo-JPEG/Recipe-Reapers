from django.db import models
from cloudinary.models import CloudinaryField


class Recipe(models.Model):
    """
    For the recipe model, ingredients have their own model
    so we can add as many as we need
    """

    title = models.CharField(max_length=100, blank=False, null=False)
    image = CloudinaryField(null=True, blank=True)
    recipe = models.TextField()

    def __str__(self):
        return self.title
