import os

from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='django-cked',
    version='0.1.2',
    author='Future Colors (original by Svyatoslav Bulbakha)',
    author_email='info@futurecolors.ru',
    description='CKEditor and elFinder integration for Django Framework.',
    url='https://github.com/simon-db/django-cked',
    packages=find_packages(),
    long_description=README,
    include_package_data=True,
    install_requires=[
        'django',
        'pytils'
    ],
)
