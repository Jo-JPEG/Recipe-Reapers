from django.db import models
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator


class Recipe(models.model):
    """
    For the recipe model, ingredients have their own model
    so we can add as many as we need
    """

    title = models.CharField(max_length=100, blank=False, null=False)
    image = CloudinaryField(null=True, blank=True)
    instructions = models.TextField()


class Ingredient(models.Model):
    """Model for each individual ingredient required for Recipe"""

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="ingredients"
    )

    name = models.CharField(max_length=100, blank=False, null=False)
    weight_in_g = models.IntegerField(validators=[MinValueValidator(1)])
