from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
# from django.contrib.auth.views import LoginView, LogoutView
#Когда регистрируетесь на сайте - получаете токен - строка выше реализует функционал получения токена



urlpatterns = [
   # path('login/', views.SignUp.as_view(), name='login'),
   path('register/', views.register, name='register'),
   # path('register/', views.UserRegister.as_view(), name='register'),
   # path('reset_password/', LoginView.as_view(template_name='users/reset_password.html')),
   # path('logout/', LogoutView.as_view(template_name='users/logout.html'))
   path('login/', views.user_login, name='login'),
   path('logout/', LogoutView.as_view(), name='logout'),
]