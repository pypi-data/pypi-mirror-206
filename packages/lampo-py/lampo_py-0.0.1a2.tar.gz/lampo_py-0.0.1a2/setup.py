# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lampo_py']

package_data = \
{'': ['*']}

install_requires = \
['cffi>=1.15.1,<2.0.0']

setup_kwargs = {
    'name': 'lampo-py',
    'version': '0.0.1a2',
    'description': '',
    'long_description': '# Python Language Binding for Lampo\n\n## What is lampo?\n\nlampo (lightning in Italian) is a experimental implementation of a tiny lightning node\n',
    'author': 'Vincenzo Palazzo',
    'author_email': 'vincenzopalazzodev@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
