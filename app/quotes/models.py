from django.db import models

class BTCPrice(models.Model):
    price = models.FloatField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
