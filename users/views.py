from django.contrib.auth.views import LoginView, LogoutView

from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # username = form.cleaned_data['username']
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # email = form.cleaned_data['email']
            # password = form.cleaned_data['password']
            # user = User(username=username, first_name=first_name, last_name=last_name,
            #             email=email, password=password)
            # user.save()
            # User(**form.cleaned_data).save()
            # User.save()
            form.save()
            return redirect('recipes:make_recipe')  # перенаправление на главную страницу
    else:
        form = UserRegistrationForm()

    return render(request, 'users/registration.html', {'form': form})

# class UserRegister(CreateView):
#     form_class = UserRegistrationForm
#     template_name = 'users/registration.html'
#     success_url = reverse_lazy('index')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('recipes:make_recipe')
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})

