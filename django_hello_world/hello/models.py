from django.db import models

# Test model
class Host(models.Model):
    user = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
