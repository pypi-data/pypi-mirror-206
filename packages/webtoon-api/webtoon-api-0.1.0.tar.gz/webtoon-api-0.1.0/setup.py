# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['webtoon_api']

package_data = \
{'': ['*']}

install_requires = \
['pycryptodome>=3.17,<4.0', 'requests>=2.29.0,<3.0.0']

setup_kwargs = {
    'name': 'webtoon-api',
    'version': '0.1.0',
    'description': 'A python library for communicating with non-public Webtoon API.',
    'long_description': '',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
