from django.db import models


class SimpleCharModel(models.Model):
    name = models.CharField(max_length=50)


class SimpleIntModel(models.Model):
    value = models.IntegerField()


class ComplexModel(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField()
    is_true = models.BooleanField()
    created = models.DateTimeField()


class RelationModel(models.Model):
    other = models.ForeignKey(SimpleCharModel, on_delete=models.CASCADE)
