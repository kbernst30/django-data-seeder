import datetime
import random

from django.test import TestCase

from data_seeder.base import DataSeeder

from . import models


class TestSimpleCharModelRandomSeed(TestCase):

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


class TestSimpleIntModelRandomSeed(TestCase):

    def test_create_single(self):
        DataSeeder(models.SimpleIntModel).seed()
        self.assertEqual(models.SimpleIntModel.objects.count(), 1)

    def test_create_many(self):
        seeds = random.randint(1, 10)
        DataSeeder(models.SimpleIntModel, seeds=seeds).seed()
        self.assertEqual(models.SimpleIntModel.objects.count(), seeds)

    def test_value(self):
        DataSeeder(models.SimpleIntModel).seed()
        simple_model = models.SimpleIntModel.objects.first()

        self.assertIsNotNone(simple_model)
        self.assertIsNotNone(simple_model.value)
        self.assertTrue(type(simple_model.value), int)


class TestComplexModelRandomSeed(TestCase):

    def test_create_single(self):
        DataSeeder(models.ComplexModel).seed()
        self.assertEqual(models.ComplexModel.objects.count(), 1)

    def test_create_many(self):
        seeds = random.randint(1, 10)
        DataSeeder(models.ComplexModel, seeds=seeds).seed()
        self.assertEqual(models.ComplexModel.objects.count(), seeds)

    def test_values(self):
        DataSeeder(models.ComplexModel).seed()
        complex_model = models.ComplexModel.objects.first()

        self.assertIsNotNone(complex_model)

        self.assertIsNotNone(complex_model.name)
        self.assertTrue(len(complex_model.name) > 0)
        self.assertTrue(type(complex_model.name), str)

        self.assertIsNotNone(complex_model.value)
        self.assertTrue(type(complex_model.value), int)

        self.assertIsNotNone(complex_model.is_true)
        self.assertTrue(type(complex_model.is_true), bool)

        self.assertIsNotNone(complex_model.created)
        self.assertTrue(type(complex_model.created), datetime.datetime)


class TestRelationModelRandomSeed(TestCase):

    def test_create_single(self):
        DataSeeder(models.RelationModel, generate_related=True).seed()
        self.assertEqual(models.RelationModel.objects.count(), 1)
        self.assertEqual(models.SimpleCharModel.objects.count(), 1)

    def test_create_many(self):
        seeds = random.randint(1, 10)
        DataSeeder(
            models.RelationModel,
            seeds=seeds,
            generate_related=True
        ).seed()

        self.assertEqual(models.RelationModel.objects.count(), seeds)
        self.assertEqual(models.SimpleCharModel.objects.count(), 1)

    def test_value(self):
        DataSeeder(models.RelationModel, generate_related=True).seed()
        relation_model = models.RelationModel.objects.first()

        self.assertIsNotNone(relation_model)
        self.assertIsNotNone(relation_model.other)
        self.assertTrue(type(relation_model.other), models.SimpleCharModel)


class TestComplexModelValueSeed(TestCase):

    def setUp(self):
        self.values = {
            "name": "John Doe",
            "value": 10,
            "is_true": True,
            "created": datetime.datetime.now()
        }

    def test_create_single(self):
        DataSeeder(models.ComplexModel, values=self.values).seed()
        self.assertEqual(models.ComplexModel.objects.count(), 1)

    def test_create_many(self):
        seeds = random.randint(1, 10)
        DataSeeder(models.ComplexModel, seeds=seeds, values=self.values).seed()
        self.assertEqual(models.ComplexModel.objects.count(), seeds)

    def test_values(self):
        seeds = random.randint(1, 10)
        DataSeeder(models.ComplexModel, seeds=seeds, values=self.values).seed()

        for complex_model in models.ComplexModel.objects.all():
            self.assertEqual(complex_model.name, self.values["name"])
            self.assertEqual(complex_model.value, self.values["value"])
            self.assertEqual(complex_model.is_true, self.values["is_true"])
            self.assertEqual(complex_model.created, self.values["created"])
