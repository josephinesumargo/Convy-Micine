from django.urls import path
from . import views
from .views import Home, RegisterPage, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('signin/', CustomLoginView.as_view(), name="signin"),
    path('signout/', LogoutView.as_view(next_page="home"), name="signout"),
    path('signup/', RegisterPage.as_view(), name="signup"),
]