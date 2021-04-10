from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.urls import reverse_lazy


class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy("registered")


class UserRegisterSuccessView(TemplateView):
    template_name = "registered.html"
