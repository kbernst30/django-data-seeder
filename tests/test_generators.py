from unittest import TestCase
from decimal import Decimal

from data_seeder import generators


class TestStaticGenerator(TestCase):

    def setUp(self):
        self.generator = generators.StaticGenerator("Hello World")

    def test_generate(self):
        value = self.generator.generate()
        self.assertEqual(value, "Hello World")


class TestNoneGenerator(TestCase):

    def setUp(self):
        self.generator = generators.NoneGenerator()

    def test_generate(self):
        value = self.generator.generate()
        self.assertIsNone(value)


class TestBooleanGenerator(TestCase):

    def setUp(self):
        self.generator = generators.BooleanGenerator()

    def test_generate(self):
        value = self.generator.generate()
        self.assertIsNotNone(value)
        self.assertEquals(type(value), bool)


class TestIntegerGenerator(TestCase):

    def setUp(self):
        self.generator = generators.IntegerGenerator()

    def test_generate(self):
        value = self.generator.generate()
        self.assertIsNotNone(value)
        self.assertEquals(type(value), int)


class TestIntegerGeneratorWithRange(TestCase):

    def setUp(self):
        self.generator = generators.IntegerGenerator(
            range_min=10,
            range_max=20
        )

    def test_generate(self):
        value = self.generator.generate()
        self.assertIsNotNone(value)
        self.assertEquals(type(value), int)
        self.assertTrue(value >= 10 and value <= 20)


class TestPositiveIntegerGenerator(TestCase):

    def setUp(self):
        self.generator = generators.PositiveIntegerGenerator()

    def test_generate(self):
        value = self.generator.generate()
        self.assertIsNotNone(value)
        self.assertEquals(type(value), int)
        self.assertTrue(value >= 0)


class TestNegativeIntegerGenerator(TestCase):

    def setUp(self):
        self.generator = generators.NegativeIntegerGenerator()

    def test_generate(self):
        value = self.generator.generate()
        self.assertIsNotNone(value)
        self.assertEquals(type(value), int)
        self.assertTrue(value < 0)


class TestFloatGenerator(TestCase):

    def setUp(self):
        self.generator = generators.FloatGenerator()

    def test_generate(self):
        value = self.generator.generate()
        self.assertIsNotNone(value)
        self.assertEquals(type(value), float)


class TestFloatGeneratorWithRange(TestCase):

    def setUp(self):
        self.generator = generators.FloatGenerator(
            range_min=10,
            range_max=20
        )

    def test_generate(self):
        value = self.generator.generate()
        self.assertIsNotNone(value)
        self.assertEquals(type(value), float)
        self.assertTrue(value >= 10 and value <= 20)


class TestPositiveFloatGenerator(TestCase):

    def setUp(self):
        self.generator = generators.PositiveFloatGenerator()

    def test_generate(self):
        value = self.generator.generate()
        self.assertIsNotNone(value)
        self.assertEquals(type(value), float)
        self.assertTrue(value >= 0)


class TestNegativeFloatGenerator(TestCase):

    def setUp(self):
        self.generator = generators.NegativeFloatGenerator()

    def test_generate(self):
        value = self.generator.generate()
        self.assertIsNotNone(value)
        self.assertEquals(type(value), float)
        self.assertTrue(value < 0)


class TestDecimalGenerator(TestCase):

    def setUp(self):
        self.generator = generators.DecimalGenerator()

    def test_generate(self):
        value = self.generator.generate()
        self.assertIsNotNone(value)
        self.assertEquals(type(value), Decimal)


class TestDecimalGeneratorWithRange(TestCase):

    def setUp(self):
        self.generator = generators.DecimalGenerator(
            range_min=10,
            range_max=20
        )

    def test_generate(self):
        value = self.generator.generate()
        self.assertIsNotNone(value)
        self.assertEquals(type(value), Decimal)
        self.assertTrue(value >= 10 and value <= 20)


class TestPositiveDecimalGenerator(TestCase):

    def setUp(self):
        self.generator = generators.PositiveDecimalGenerator()

    def test_generate(self):
        value = self.generator.generate()
        self.assertIsNotNone(value)
        self.assertEquals(type(value), Decimal)
        self.assertTrue(value >= 0)


class TestNegativeDecimalGenerator(TestCase):

    def setUp(self):
        self.generator = generators.NegativeDecimalGenerator()

    def test_generate(self):
        value = self.generator.generate()
        self.assertIsNotNone(value)
        self.assertEquals(type(value), Decimal)
        self.assertTrue(value < 0)


class TestStringGenerator(TestCase):

    def setUp(self):
        self.generator = generators.StringGenerator(max_length=30)

    def test_generate(self):
        value = self.generator.generate()
        self.assertIsNotNone(value)
        self.assertEquals(type(value), str)
        self.assertTrue(len(value) <= 30)
