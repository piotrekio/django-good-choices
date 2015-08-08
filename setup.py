from distutils.core import setup


setup(
    name = 'django-good-choices',
    version = '1.5',
    description = 'Simple and convenient approach to "choices" in Django',
    author = 'Piotr Wasilewski',
    author_email = 'piotrek@piotrek.io',
    url = 'https://github.com/piotrekio/django-good-choices',
    py_modules = ['good_choices'],
    install_requires = ['six==1.9.0']
)
