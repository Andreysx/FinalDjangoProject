from django.urls import path
from . import views
# from django.contrib.auth.views import LoginView, LogoutView
#Когда регистрируетесь на сайте - получаете токен - строка выше реализует функционал получения токена

urlpatterns = [
   path('signup/', views.SignUp.as_view()),
   path('login/', views.MyLoginView.as_view(), name='login'),
   # path('reset_password/', LoginView.as_view(template_name='users/reset_password.html')),
   # path('logout/', LogoutView.as_view(template_name='users/logout.html'))
]