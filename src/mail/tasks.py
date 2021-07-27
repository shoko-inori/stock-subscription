from celery import shared_task

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


@shared_task
def send_digest():
    all_sub = Subscription.objects.all()
    ticker_string = ""
    email_dict = {}
    for sub in all_sub:
        # Compose the parameter for the API call to fetch prices
        ticker_string = "{} {}".format(ticker_string, sub.ticker)
        # Categorize the subscriptions based on the mailto email address
        if sub.email in email_dict:
            email_dict[sub.email][sub.ticker] = 0
        else:
            email_dict[sub.email] = {sub.ticker: 0}

    # Make the API call and feed the fetched prices to the categorized dict
    yf_response = yf.Tickers(ticker_string.strip())
    for sub in all_sub:
        email_dict[sub.email][sub.ticker] = yf_response.tickers[sub.ticker].info["regularMarketPrice"]

    # Send the messages
    for mailto in email_dict:
        send_email_task(mailto, email_dict[mailto])

    return None
