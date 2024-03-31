from django.urls import path

from .views import recipe_review, index, make_recipe, update_recipe

app_name = 'recipes'

urlpatterns = [
   path('', index, name='index'),
   path('full_recipe/<int:recipe_id>/', recipe_review, name='recipe_review'),
   path('new_recipe', make_recipe, name='make_recipe'),
   path('update_recipe/<int:recipe_id>/', update_recipe, name='update_recipe'),
]