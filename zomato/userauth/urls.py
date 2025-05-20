from django.urls import path
import userauth.views as views


urlpatterns = [
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("data/", views.data, name="data"),
]