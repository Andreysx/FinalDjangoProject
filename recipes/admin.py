from django.contrib import admin
from .models import Category, Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    #настройка отображения
    list_display = ['title', 'description', 'cooking_time',  'cooking_steps']
    #добавление фильтрации
    list_filter = ['title']
    list_editable = ['description', 'cooking_steps']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    #настройка отображения
    list_display = ['name']
    #добавление фильтрации
    list_filter = ['name']


