from django import forms


class SubscriptionForm(forms.Form):
    ticker = forms.CharField(max_length=5)
    email = forms.EmailField()
