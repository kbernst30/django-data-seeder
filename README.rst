==================
django-data-seeder
==================

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
