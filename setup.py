# -*- coding:utf-8 -*-
from distutils.core import setup
from djrestlet import __version__

setup(name='django-restlet',
      version=__version__,
      description='RESTful extention on Django.',
      long_description=open("README.md").read(),
      author='Mingcai SHEN',
      author_email='archsh@gmail.com',
      packages=['djrestlet'],
      package_dir={'djrestlet': 'djrestlet'},
      package_data={'djrestlet': ['stuff']},
      license="Public domain",
      platforms=["any"],
      install_requires=[
          'Django>=1.4.5',
          'simplejson>=2.3.2',
          'PyYAML>=3.10',
      ],
      url='https://github.com/archsh/django-restlet')
