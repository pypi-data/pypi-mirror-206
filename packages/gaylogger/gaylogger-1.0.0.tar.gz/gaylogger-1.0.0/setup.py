# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gaylogger']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'gaylogger',
    'version': '1.0.0',
    'description': '',
    'long_description': None,
    'author': 'ArshiAAkhavan',
    'author_email': 'letmemakenewone@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
