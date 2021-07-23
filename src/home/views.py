from django.shortcuts import render
from .forms import SubscriptionForm


# Create your views here.
def home_view(request):
    return render(request, "home.html", {})


def subscribe_view(request):
    subscription_form = SubscriptionForm()
    context = {
        "subscription_form": subscription_form
    }
    return render(request, "subscribe.html", context)
