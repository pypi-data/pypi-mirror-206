# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dfl']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pydfl',
    'version': '0.1.0',
    'description': 'Toolsets for transforming and searching the path of dfl(Directory, File, Link)',
    'long_description': '# dfl\nToolsets for transforming and searching the path of dfl(Directory, File, Link)\n',
    'author': 'Doohoon Kim',
    'author_email': 'me@doohoon.kim',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
