from django import forms
from .models import Recipe, Category


class RecipeForm(forms.ModelForm):
    title = forms.CharField(max_length=100,
                            label="Наименование блюда",
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Наименование блюда'}))
    description = forms.CharField(max_length=250,
                                  label="Описание блюда",
                                  widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание блюда'}))
    cooking_steps = forms.CharField(max_length=10000,
                                    label="Как приготовить",
                                    widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Как приготовить'}))
    cooking_time = forms.TimeField(label="Время приготовления",
                                   help_text='Укажите время приготовления блюда',
                                   widget=forms.TimeInput(format='%H:%M', attrs={'type': 'time'}))
    ingredients = forms.CharField(max_length=200,
                                  label="Ингридиенты",
                                  widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ингридиенты'}))

    category = forms.ModelChoiceField(label='Выберите категорию', queryset=Category.objects.all())

    image = forms.ImageField(label="Изображение блюда", widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Recipe
        fields = ('title', 'description', 'cooking_steps', 'cooking_time')