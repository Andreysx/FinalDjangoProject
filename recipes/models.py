from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f' Имя категории: {self.name}'


class Recipe(models.Model):
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=200)
    cooking_steps = models.TextField(blank=True)
    cooking_time = models.TimeField()
    ingredients = models.TextField()
    image = models.ImageField(upload_to='recipe_image/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    categories = models.ManyToManyField(Category, through='RecipeCategory', related_name='recipes')

    def __str__(self):
        return f'{self.title}, {self.cooking_time}, {self.author}'


class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)