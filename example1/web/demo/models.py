from django.db import models


class Pizza(models.Model):
    '''Docs:
    https://docs.djangoproject.com/en/1.9/ref/models/fields/
    '''
    name = models.CharField(max_length=30)
    description = models.TextField()
    cost = models.DecimalField(max_digits=5, decimal_places=2)

