import random

from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, Category
from .forms import RecipeForm


def index(request):
    recipes = Recipe.objects.all()
    random_recipes = []
    for i in range(5):
        random_recipes.append(random.choice(recipes))
    return render(request, 'recipes/index.html', {'random_recipes': random_recipes})

# def index(request):
#     recipes = Recipe.objects.order_by('?')[:5]
#     return render(request, 'recipes/index.html', {'recipes': recipes})


def recipe_review(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/recipe_review.html', {'recipe': recipe})


def make_recipe(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = RecipeForm(request.POST, request.FILES)
            message = 'Ошибка данных'
            if form.is_valid():
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                cooking_steps = form.cleaned_data['cooking_steps']
                cooking_time = form.cleaned_data['cooking_time']
                ingredients = form.cleaned_data['ingredients']
                image = form.cleaned_data['image']
                fs = FileSystemStorage()
                fs.save(image.name, image)
                author = request.user
                recipe = Recipe(title=title, description=description, cooking_steps=cooking_steps,
                                cooking_time=cooking_time, ingredients=ingredients,
                                image=image, author=author)
                recipe.save()
                message = 'Рецепт сохранен'
        else:
            form = RecipeForm()
            message = 'Заполните форму создания рецепта'
        return render(request, 'recipes/make_recipe.html', {'form': form, 'message': message})
    else:
        return redirect('login')


# @login_required
def update_recipe(request, recipe_id):
    if request.user.is_authenticated:
        message = 'Ошибка данных'
        if request.method == 'POST':
            form = RecipeForm(request.POST, request.FILES)
            if form.is_valid():
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                cooking_steps = form.cleaned_data['cooking_steps']
                cooking_time = form.cleaned_data['cooking_time']
                ingredients = form.cleaned_data['ingredients']
                image = form.cleaned_data['image']
                fs = FileSystemStorage()
                fs.save(image.name, image)
                author = request.user
                recipe = Recipe(title=title, description=description, cooking_steps=cooking_steps,
                                cooking_time=cooking_time, ingredients=ingredients,
                                image=image, author=author)
                recipe.save()
                message = 'Рецепт изменён'
        else:
            form = RecipeForm()
            message = 'Заполните форму для изменения рецепта'
        return render(request, 'recipes/make_recipe.html', {'form': form, 'message': message})
    else:
        return redirect('login')