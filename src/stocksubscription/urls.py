"""stocksubscription URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from home.views import home_view, subscribe_view, delete_view
from mail.views import send_email_view
from register.views import register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    path('register/', register_view, name="register"),
    path('', include("django.contrib.auth.urls")),
    path('subscribe/', subscribe_view, name="subscribe"),
    path('<int:sub_id>/unsubscribe/', delete_view, name="unsubscribe"),
    path('<int:sub_id>/send-mail/', send_email_view, name="send_mail"),
]
