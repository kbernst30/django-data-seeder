==================
django-data-seeder
==================

|build| |package|

This app provides a simple way of seeding data for your data models into your
development or test database. This can be achieved through the Admin site, via
a management command, or by writing your own scripts that use a seeder object.

It is often necessary to be able to seed large datasets, especially in complex
projects, where having pre-loaded data can save time in the development
lifecycle. Additionally, by allowing simple data seeding, you can more
effectively conduct load tests or test complex edge case scnearios.

Requirements
============

* Django 2.2+
* Python 3.6+

Installation
============

You can install ``data_seeder`` using ``pip``

.. code-block:: bash

    pip install django-data-seeder


Quick Start
===========

1. Add ``data_seeder`` to your ``INSTALLED_APPS`` in ``settings.py``

   .. code-block:: python

     INSTALLED_APPS = [
       ...

       'data_seeder',
     ]

2. Seed data with the following command

   .. code-block:: bash

     python manage.py seeddata [options] app.models.Model [app.models.Model2, ...]

   This will generate a single seed for each model provided.


Advanced Usage of the Management Command
========================================

In addition to generating single seeds for models, the ``seeddata`` can
also create as many seeds as you want

.. code-block:: bash

  python manage.py seeddata --seeds=N apps.model.Model

This will generate ``N`` seeds for ``apps.model.Model``

Another option that you can use is to generate related models. This is
used for foreign key references where we need to recursively generate
seeds for models. The default behaviour for this is disabled, meaning
that a randomly selected existing model will be used for the related
model field. We override this by doing the following

.. code-block:: bash

  python manage.py seeddata --generate-related apps.model.Model

One limitation to this behavior is that the data seeder will not generate
a related model if the relation is the model itself. This would cause an
infinite recursion.

For more information about the ``seeddata`` command, please look at the
help page.

.. code-block:: bash

  python manage.py help seeddata


Using the Django Admin Site
===========================

For convenience, you can also use the out-of-the-box Administrator site
included with Django to generate your seeds.

To do this, you must register your models with the admin site using the
custom ``ModelAdmin`` class provided. For example, in ``admin.py`` for
your app

.. code-block:: python

  from django.contrib import admin

  from .models import MyModel
  from data_seeder.admin import DataGeneratorAdmin

  admin.site.register(MyModel, DataGeneratorAdmin)

This will add a button to the model page in the admin site to generate
data, which will provide you with the same options available in the
management command.

You can also register your models using a decorator instead

.. code-block:: python

  from django.contrib import admin

  from .models import MyModel
  from data_seeder.admin import data_generator_register

  @admin.register(MyModel)
  @data_generator_register
  class MyModelAdmin(admin.ModelAdmin):
      pass


Contribute
==========

You can find the latest development version on GitHub_. Feel free to
fork it, file bugs, or contribute.

Feel free to send me a message by email_ or twitter_.

.. _GitHub: https://github.com/kbernst30/django-data-seeder

.. _email: mailto:kbernst30@gmail.com

.. _twitter: https://twitter.com/kbernst30

.. |build| image:: https://circleci.com/gh/kbernst30/django-data-seeder.svg?style=shield
    :target: https://circleci.com/gh/kbernst30/django-data-seeder

.. |package| image:: https://badge.fury.io/py/django-data-seeder.svg
    :alt: Package Version
    :scale: 100%
    :target: http://badge.fury.io/py/django-data-seeder
