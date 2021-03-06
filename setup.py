from setuptools import setup

setup(
    name = 'facebook-internal-module',
    version = '0.1.3',
    author = 'Krzysztof Hoffmann',
    author_email = 'krzysiekpl@gmail.com',
    license='BSD',
    url = 'https://github.com/hoffmannkrzysztof/facebook-internal-module',
    packages = ['extfacebook','extwebsite'],
    install_requires= [
        'celery',
        'django-celery',
        'facepy',
        'python-dateutil'
    ],
    )
