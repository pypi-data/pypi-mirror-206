# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zconf']

package_data = \
{'': ['*']}

install_requires = \
['omegaconf>=2.3.0,<3.0.0',
 'pydfl>=0.1.0,<0.2.0',
 'python-dotenv>=1.0.0,<2.0.0']

setup_kwargs = {
    'name': 'pyzconf',
    'version': '0.1.2',
    'description': '',
    'long_description': '# zconf\nEasy configurations to python classes variables with conf files.\n',
    'author': 'Doohoon Kim',
    'author_email': 'invi.dh.kim@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
