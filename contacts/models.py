from datetime import datetime
from django.db import models
from django.db.models import base

from datetime import datetime

class Contacts(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    customer_need=models.CharField(max_length=255)
    car_title=models.CharField(max_length=255)
    car_id=models.IntegerField()
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    message=models.TextField(blank=True)
    phone=models.CharField(max_length=255)
    user_id=models.IntegerField(blank=True)
    email=models.EmailField(max_length=100)
    created_date=models.DateTimeField(blank=True,default=datetime.now)

    def __str__(self):
        return self.email
