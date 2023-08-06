# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bia_rembi_models']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'bia-rembi-models',
    'version': '0.1.0',
    'description': '',
    'long_description': 'None',
    'author': 'Matthew Hartley',
    'author_email': 'matthewh@ebi.ac.uk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
