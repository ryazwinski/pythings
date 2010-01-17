from setuptools import setup
setup(
    name='pythings',
    py_modules=['pythings'],
    version='0.1',
    description='Python Library for interfacing with Withings API',
    install_requires=['simplejson', 'urllib2', 'hashlib'],
)

