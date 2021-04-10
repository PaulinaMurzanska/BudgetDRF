from django.urls import path
from .views import UserRegisterView, UserRegisterSuccessView


urlpatterns = [
    path("/register/", UserRegisterView.as_view(), name="register"),
    path("/registered", UserRegisterSuccessView.as_view(), name="registered")

]