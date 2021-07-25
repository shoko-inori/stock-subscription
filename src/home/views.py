from django.shortcuts import render, redirect, get_object_or_404
from .forms import SubscriptionForm
from .models import Subscription
import yfinance as yf

# Create your views here.
def home_view(request):
    # Redirect to login page for unauthorized users
    if not request.user.is_authenticated:
        return redirect("login/")

    context = {"subscriptions": []}

    # Compose and make API call to fetch prices
    all_sub = request.user.subscription.all()
    sub_string = ""
    for sub in all_sub:
        sub_string = "{} {}".format(sub_string, sub.ticker)
    yf_response = yf.Tickers(sub_string.strip())

    # Render the subscription list table
    for sub in all_sub:
        context["subscriptions"].append({
            "id": sub.id,
            "ticker": sub.ticker,
            "current_price": yf_response.tickers[sub.ticker].info["regularMarketPrice"],
            "email": sub.email
        })
    return render(request, "home.html", context)


def subscribe_view(request):
    subscription_form = SubscriptionForm()
    if request.method == "POST":
        subscription_form = SubscriptionForm(request.POST)
        if subscription_form.is_valid():
            ticker, email = \
                subscription_form.cleaned_data["ticker"].upper(), subscription_form.cleaned_data["email"]
            sub = Subscription(ticker=ticker, email=email)
            sub.save()
            request.user.subscription.add(sub)

            return redirect("/")

    context = {
        "subscription_form": subscription_form
    }
    return render(request, "subscribe.html", context)


def delete_view(request, sub_id):
    sub = get_object_or_404(Subscription, id=sub_id)
    if request.method == "POST":
        sub.delete()
        return redirect("/")
    context = {
        "sub": sub
    }
    return render(request, "delete.html", context)
