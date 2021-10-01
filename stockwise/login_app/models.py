from django.db import models

# Create your models here.
class User(models.Model):
    UserId = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=150)
    LastName = models.CharField(max_length=150)
    Email = models.CharField(max_length=350)
    password = models.CharField(max_length = 60)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)