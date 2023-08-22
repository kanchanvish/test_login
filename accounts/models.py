# accounts/models.py
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # Use hash and salt in production

class Referral(models.Model):
    referrer = models.ForeignKey(User, related_name='referrals_given', on_delete=models.CASCADE)
    referred_user = models.ForeignKey(User, related_name='referrals_received', on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)

