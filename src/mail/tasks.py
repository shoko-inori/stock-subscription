from celery import shared_task
from stocksubscription.celery import app
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from home.models import Subscription
import yfinance as yf


@shared_task
def send_email_task(mailto, tickers):
    # Compose the context to feed the template
    context = {
        "subscriptions": [],
    }
    for sub in tickers:
        context["subscriptions"].append({
            "ticker": sub,
            "current_price": tickers[sub],
        })

    # Send the email
    html_content = render_to_string("email_template.html", context)
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        "Latest stock prices from your subscription - Chenhao's Stock Price Subscription",
        text_content,
        "frank.gong.1006@hotmail.com",
        [mailto]
    )
    email.attach_alternative(html_content, "text/html")
    email.send()

    return None
