# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyama']

package_data = \
{'': ['*'], 'pyama': ['static/*', 'templates/*']}

install_requires = \
['Flask>=2.2.3,<3.0.0',
 'GitPython>=3.1.31,<4.0.0',
 'llama-cpp-python>=0.1.39,<0.2.0',
 'pycurl>=7.45.2,<8.0.0',
 'requests>=2.28.2,<3.0.0']

entry_points = \
{'console_scripts': ['pyama = pyama.pyama:main']}

setup_kwargs = {
    'name': 'pyama',
    'version': '0.1.0',
    'description': '"Flask frontend for llama.cpp models"',
    'long_description': '',
    'author': 'Jiri Podivin',
    'author_email': 'jpodivin@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
