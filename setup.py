import os
import sys

from setuptools import find_packages, setup
from setuptools.command.install import install

VERSION = '0.1.2'

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""

    description = 'verify that the git tag matches our version'

    def run(self):
        tag = os.getenv('CIRCLE_TAG')

        if tag != VERSION and tag != 'v' + VERSION:
            info = "Git tag: {0} does not match app version: {1}".format(
                tag, VERSION
            )

            sys.exit(info)


setup(
    name='django-data-seeder',
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    license='BSD-3-Clause',
    description='A data seeder for models for Django.',
    long_description=README,
    url='https://github.com/kbernst30/django-data-seeder/',
    author='Kyle Bernstein',
    author_email='kbernst30@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    cmdclass={
        'verify': VerifyVersionCommand,
    },
)
