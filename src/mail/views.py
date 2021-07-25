from django.shortcuts import render, redirect, get_object_or_404
from .tasks import send_email_task
from home.models import Subscription
import yfinance as yf


# Create your views here.
def send_email_view(request, sub_id):
    sub = get_object_or_404(Subscription, id=sub_id)
    send_email_task(sub.email, {
        sub.ticker: yf.Ticker(sub.ticker).info["regularMarketPrice"]
    })
    return redirect("/")
