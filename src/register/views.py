from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register_view(response):
    register_form = UserCreationForm()
    if response.method == "POST":
        register_form = UserCreationForm(response.POST)
        if register_form.is_valid():
            register_form.save()
        else:
            register_form = UserCreationForm()
    return render(response, "register.html", {"register_form": register_form})
