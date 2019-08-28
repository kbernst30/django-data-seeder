from django.db import models


class SimpleCharModel(models.Model):
    name = models.CharField(max_length=50)
