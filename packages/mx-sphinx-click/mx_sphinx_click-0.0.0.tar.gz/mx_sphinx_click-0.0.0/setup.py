# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mx_sphinx_click']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'mx-sphinx-click',
    'version': '0.0.0',
    'description': '',
    'long_description': '',
    'author': 'None',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.4,<4.0',
}


setup(**setup_kwargs)
