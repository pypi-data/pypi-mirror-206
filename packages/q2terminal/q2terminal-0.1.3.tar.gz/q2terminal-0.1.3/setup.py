# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['q2terminal']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'q2terminal',
    'version': '0.1.3',
    'description': '',
    'long_description': '# Interaction with a terminal session\n\n```\n```\n',
    'author': 'Andrei Puchko',
    'author_email': 'andrei.puchko@gmx.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
