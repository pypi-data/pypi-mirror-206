# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['harlequin']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'duckdb>=0.7.1,<0.8.0', 'textual>=0.22.3,<0.23.0']

entry_points = \
{'console_scripts': ['harlequin = harlequin.cli:harlequin']}

setup_kwargs = {
    'name': 'harlequin',
    'version': '0.0.1',
    'description': 'A Text User Interface for DuckDB',
    'long_description': '# harlequin\nA Text User Interface for DuckDB\n',
    'author': 'Ted Conbeer',
    'author_email': 'tconbeer@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
