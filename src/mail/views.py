from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .tasks import send_email_task
from home.models import Subscription



# Create your views here.
def send_email_view(request, sub_id):
    sub = get_object_or_404(Subscription, id=sub_id)
    send_email_task(sub.email, [sub])
    return redirect("/")
