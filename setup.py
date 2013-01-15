#!/usr/bin/env python
from setuptools import setup

setup(name='django-forceadminlanguage',
      version='0.0.1',
      description='Force Django Admin to show in one selected language.',
      long_description='Use one language for Django Admin in multilingual sites.',
      author='Vital Belikov',
      author_email='vital@qwe.lv',
      packages=['forceadminlanguage'],
      url='https://github.com/Brick85/django_forceadminlanguage/',
      include_package_data=True,
      zip_safe=False,
      requires=['django(>=1.3)'],
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Natural Language :: English',
                   'Operating System :: Unix',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Utilities'],
      license='New BSD')
