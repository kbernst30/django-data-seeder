from django.db import models

from . import generators


class DataSeeder:

    field_generators = [
        (models.BigIntegerField, generators.IntegerGenerator),
        (models.BooleanField, generators.BooleanGenerator),
        (models.CharField, generators.StringGenerator),
        (models.DateField, generators.DateGenerator),
        (models.DateTimeField, generators.DateTimeGenerator),
        (models.DecimalField, generators.DecimalGenerator),
        (models.EmailField, generators.EmailGenerator),
        (models.FloatField, generators.FloatGenerator),
        (models.IntegerField, generators.IntegerGenerator),
        (models.GenericIPAddressField, generators.IpAddressGenerator),
        (models.NullBooleanField, generators.BooleanGenerator),
        (models.PositiveIntegerField, generators.PositiveIntegerGenerator),
        (models.PositiveSmallIntegerField,
            generators.PositiveIntegerGenerator),
        (models.SmallIntegerField, generators.IntegerGenerator),
        (models.TextField, generators.StringGenerator),
        (models.TimeField, generators.TimeGenerator),
        (models.URLField, generators.UrlGenerator),
        (models.UUIDField, generators.UuidGenerator)
    ]

    def __init__(self, model, seeds=1, generate_related=False, values={}):
        self.model = model
        self.seeds = seeds
        self.generate_related = generate_related
        self.values = values

    def seed(self):
        seeds = []
        associated_models = {}

        for i in range(self.seeds):

            generated = self.model()

            for field in self.model._meta.fields:
                field_cls = field.__class__
                generator = self._get_generator(field_cls)

                # If this field has been provided by the generator, use that
                if field.name in self.values:
                    setattr(generated, field.name, self.values[field.name])
                    continue

                # If this is a foreign key field, we need to do some special
                # logic to get a properly generated value
                if field_cls == models.ForeignKey and self.generate_related:
                    associated_cls = field.related_model
                    association = associated_models.get(associated_cls)
                    if associated_cls != self.model and association is None:
                        # Avoid if FK is same as model, otherwise we will hit
                        # infinite recursion
                        associated = DataSeeder(associated_cls,
                                                generate_related=True).seed()

                        # There should be one entity in associated
                        association = associated[0]

                    setattr(generated, field.name, association)
                    associated_models[associated_cls] = association

                    continue

                # If the field can be generated, do so
                # There are some cases (Auto increments) where we do not
                # need to bother generating
                if generator is not None:
                    setattr(generated, field.name, generator.generate())

            generated.save()
            seeds.append(generated)

        return seeds

    def _get_generator(self, field_cls):
        for field_generator in self.field_generators:
            if field_generator[0] == field_cls:
                return field_generator[1]()

        return None
