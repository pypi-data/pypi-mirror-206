# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['coshell', 'coshell.internal', 'coshell.internal.openai']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.7,<2', 'pyperclip>=1.8.2,<2', 'requests>=2,<3']

entry_points = \
{'console_scripts': ['my_script = coshell.main:main']}

setup_kwargs = {
    'name': 'coshell',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Joshua Wycuff',
    'author_email': 'josh.wycuff@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4',
}


setup(**setup_kwargs)
