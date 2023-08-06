# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['elia_chat', 'elia_chat.widgets']

package_data = \
{'': ['*']}

install_requires = \
['openai>=0.27.5,<0.28.0', 'textual[dev]>=0.18.0']

entry_points = \
{'console_scripts': ['elia = elia.app:run']}

setup_kwargs = {
    'name': 'elia-chat',
    'version': '0.1.0',
    'description': 'A terminal interface to ChatGPT.',
    'long_description': '# Elia\n\nA quick experiment using Textual to demonstrate how you might\nbuild a ChatGPT client in the terminal.\n',
    'author': 'Darren Burns',
    'author_email': 'darrenb900@gmail.com',
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
