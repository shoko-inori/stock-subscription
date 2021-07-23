from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscription", null=True)
    ticker = models.CharField(max_length=5)
    email = models.EmailField()
