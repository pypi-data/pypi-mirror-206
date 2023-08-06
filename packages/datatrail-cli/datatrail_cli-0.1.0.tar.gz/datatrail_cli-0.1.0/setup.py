# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dtcli']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'requests>=2.29.0,<3.0.0', 'rich>=13.3.5,<14.0.0']

entry_points = \
{'console_scripts': ['datatrail = dtcli.cli:cli']}

setup_kwargs = {
    'name': 'datatrail-cli',
    'version': '0.1.0',
    'description': 'CHIME/FRB Datatrail CLI',
    'long_description': '# Datatrail User CLI\n',
    'author': 'CHIME FRB Project Office',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
