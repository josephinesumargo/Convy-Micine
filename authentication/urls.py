from django.urls import path
from . import views
from .views import Home, RegisterPage, CustomLoginView
from django.contrib.auth.views import LogoutView

app_name = 'authentication'

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('signin/', CustomLoginView.as_view(), name="signin"),
    path('signout/', LogoutView.as_view(next_page="authentication:home"), name="signout"),
    path('signup/', RegisterPage.as_view(), name="signup"),
]