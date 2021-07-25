from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import yfinance as yf
# from time import sleep


@shared_task
def send_email_task(mailto, tickers):
    # Call API to obtain latest prices of all tickers
    ticker_string = ""
    for sub in tickers:
        ticker_string = "{} {}".format(ticker_string, sub.ticker)
    yf_response = yf.Tickers(ticker_string.strip())

    # Compose the context to feed the template
    context = {
        "subscriptions": [],
    }
    for sub in tickers:
        context["subscriptions"].append({
            "ticker": sub.ticker,
            "current_price": yf_response.tickers[sub.ticker].info["regularMarketPrice"],
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
