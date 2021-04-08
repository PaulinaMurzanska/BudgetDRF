from django.views import generic
from django.contrib.auth.forms import UserCreationForm


class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "register.html"
    success_url = "http://localhost:3000/register_success"
