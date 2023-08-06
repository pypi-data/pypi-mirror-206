# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['morgan_linter']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['morgan = morgan_linter:cli']}

setup_kwargs = {
    'name': 'morgan-linter',
    'version': '1.2.1',
    'description': 'Linter to validate google docstrings',
    'long_description': '# morgan-linter\nLinter to verify the google docstrings format in a python project\n',
    'author': 'Edwar Girón',
    'author_email': 'contactoedwargiron@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
