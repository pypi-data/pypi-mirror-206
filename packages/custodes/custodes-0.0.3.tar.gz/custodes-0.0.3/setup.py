# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['custodes']

package_data = \
{'': ['*']}

install_requires = \
['aio-pika>=9.0.5,<10.0.0',
 'aiohttp>=3.8.4,<4.0.0',
 'codefast>=23.4.18.13,<24.0.0.0',
 'rich>=13.3.5,<14.0.0',
 'simauth>=0.0.8,<0.0.9']

setup_kwargs = {
    'name': 'custodes',
    'version': '0.0.3',
    'description': '',
    'long_description': '\nApp guardians.\n\n',
    'author': 'tompz',
    'author_email': 'tompz@tompz.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
