# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['regenbib']

package_data = \
{'': ['*']}

install_requires = \
['arxiv>=1.4.7,<2.0.0',
 'beautifulsoup4>=4.12.2,<5.0.0',
 'bibtex-dblp>=0.5,<0.6',
 'marshmallow-dataclass[enum,union]==8.5.11',
 'requests>=2.29.0,<3.0.0']

entry_points = \
{'console_scripts': ['regenbib = regenbib.cli_render:run',
                     'regenbib-import = regenbib.cli_import:run']}

setup_kwargs = {
    'name': 'regenbib',
    'version': '0.0.2',
    'description': '(Re-)generate tidy .bib files from online sources',
    'long_description': '# regenbib\n(Re-)generate tidy .bib files from online sources\n',
    'author': 'Joachim Neu',
    'author_email': 'jneu@stanford.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/joachimneu/regenbib',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
