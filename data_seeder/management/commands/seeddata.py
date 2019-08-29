'''
Adds the seeddata management command for Django manage.py
'''

import importlib

from django.core.management.base import BaseCommand, CommandError
from django.db.models import Model

from ...base import DataSeeder


class Command(BaseCommand):
    '''
    The command class

    This command creates the seeddata command for manage.py.
    By running this command, we can create data seeds for
    development and test DBs

    Attributes
    ----------
    help : str
        the help text for this command
    '''

    help = "Seeds random data into the supplied model(s)"

    def add_arguments(self, parser):
        parser.add_argument('models', nargs='+', type=str)

        # Optional arguments
        parser.add_argument(
            '--seeds',
            help='Specify the number of seeds to generate'
        )

        parser.add_argument(
            '--generate-related',
            action='store_true',
            help='Generate foreign key relations instead of using random model'
        )

    def handle(self, *args, **options):
        models = self._get_models(options["models"])
        seeds = int(options["seeds"]) if options["seeds"] else 1
        generate_related = options["generate_related"] \
            if options["generate_related"] else False

        for model in models:
            self.stdout.write(self.style.WARNING('\nSeeding data for "%s"...' %
                                                 model.__name__))

            DataSeeder(model, seeds=seeds,
                       generate_related=generate_related).seed()

            self.stdout.write(self.style.SUCCESS('Seed(s) for "%s" complete' %
                                                 model.__name__))

    def _get_models(self, model_paths):
        models = []
        for module_name in model_paths:
            try:
                # Get the model name from the module
                module_parts = module_name.split(".")
                model_name = module_parts[-1]

                # Module should not include the model name
                module_path = ".".join(module_parts[:-1])
                module = importlib.import_module(module_path)

                # Get and verify model
                model = getattr(module, model_name)
                if not issubclass(model, Model):
                    raise CommandError('Class "%s" is not a valid model' %
                                       module_name)

                models.append(model)

            except (ModuleNotFoundError, AttributeError):
                raise CommandError('Class "%s" does not exist' % module_name)

        return models
