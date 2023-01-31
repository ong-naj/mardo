from django.urls import path
from .views import login_naj
urlpatterns= [
    path('login', login_naj, name='login-naj')

]