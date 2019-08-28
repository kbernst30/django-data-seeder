import random
from django.test import TestCase

from data_seeder.base import DataSeeder

from . import models


class TestSimpleCharModel(TestCase):

    def test_create_single(self):
        DataSeeder(models.SimpleCharModel).seed()
        self.assertEqual(models.SimpleCharModel.objects.count(), 1)

    def test_create_many(self):
        seeds = random.randint(1, 10)
        DataSeeder(models.SimpleCharModel, seeds=seeds).seed()
        self.assertEqual(models.SimpleCharModel.objects.count(), seeds)

    def test_value(self):
        DataSeeder(models.SimpleCharModel).seed()
        simple_model = models.SimpleCharModel.objects.first()

        self.assertIsNotNone(simple_model)
        self.assertIsNotNone(simple_model.name)
        self.assertTrue(len(simple_model.name) > 0)
        self.assertTrue(type(simple_model.name), str)
