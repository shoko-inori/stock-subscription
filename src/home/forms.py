from django import forms
import yfinance as yf


class SubscriptionForm(forms.Form):
    ticker = forms.CharField(max_length=5)
    email = forms.EmailField()

    def clean_ticker(self):
        ticker = self.cleaned_data.get("ticker")
        # All API to check if the ticker is valid
        if yf.Ticker(ticker).info["regularMarketPrice"]:
            return ticker
        else:
            raise forms.ValidationError("This ticker is not valid. Please try another ticker. ")
