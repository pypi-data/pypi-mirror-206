# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['enalog_cli']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.29.0,<3.0.0', 'typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['enalog = enalog_cli.main:app']}

setup_kwargs = {
    'name': 'enalog-cli',
    'version': '0.1.1',
    'description': 'EnaLog CLI',
    'long_description': '# EnaLog CLI\n\n## Installation\n\n`pip install --user enalog-cli`\n\n## Usage\n\n* Pushing an event to EnaLog: \n```sh\nenalog push --api-token=<api-token> --event=\'{"project":"<project-name>","name":"<event-name>","push":false}\'\n```',
    'author': 'Sam Newby',
    'author_email': 'sam@enalog.app',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
