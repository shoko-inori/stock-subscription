from django.shortcuts import render
from .forms import SubscriptionForm
from .models import Subscription


# Create your views here.
def home_view(request):
    return render(request, "home.html", {})


def subscribe_view(request):
    subscription_form = SubscriptionForm()
    if request.method == "POST":
        subscription_form = SubscriptionForm(request.POST)
        if subscription_form.is_valid():
            ticker, email = \
                subscription_form.cleaned_data["ticker"], subscription_form.cleaned_data["email"]
            sub = Subscription(ticker=ticker, email=email)
            sub.save()
            request.user.subscription.add(sub)

    context = {
        "subscription_form": subscription_form
    }
    return render(request, "subscribe.html", context)
