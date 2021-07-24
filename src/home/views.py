from django.shortcuts import render, redirect
from .forms import SubscriptionForm
from .models import Subscription
import yfinance as yf

# Create your views here.
def home_view(request):
    context = {"subscriptions": []}
    for sub in request.user.subscription.all():
        context["subscriptions"].append({
            "ticker": sub.ticker,
            "current_price": yf.Ticker(sub.ticker).info["regularMarketPrice"],
            "email": sub.email
        })
    return render(request, "home.html", context)


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

            return redirect("/")

    context = {
        "subscription_form": subscription_form
    }
    return render(request, "subscribe.html", context)
