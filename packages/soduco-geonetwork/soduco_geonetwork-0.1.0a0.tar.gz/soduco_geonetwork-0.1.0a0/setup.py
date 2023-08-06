# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['soduco_geonetwork', 'soduco_geonetwork.api_wrapper', 'soduco_geonetwork.cli']

package_data = \
{'': ['*'], 'soduco_geonetwork.api_wrapper': ['xmltemplates/*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'click>=8.1.3,<9.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'requests>=2.28.1,<3.0.0']

entry_points = \
{'console_scripts': ['soduco_geonetwork_cli = soduco_geonetwork.cli.cli:cli']}

setup_kwargs = {
    'name': 'soduco-geonetwork',
    'version': '0.1.0a0',
    'description': 'A python wrapper to use Geonetwork API',
    'long_description': "# Geonetwork Python client\n\nThis package helps you create XML files for the Geonetwork metadata catalog and handle its API.\nIt's currently in alpha release.\n\n## Commands\n\nHere are the available commands:\n\n\n```bash\n    soduco_geonetwork_cli parse\n```\nParse a yaml file and create xml files accordingly\n\n```bash\n    soduco_geonetwork_cli upload\n```\nUpload xml files listed in a csv file\n\n```bash\n    soduco_geonetwork_cli delete\n```\nDelete records on geonetwork from a uuid list in a csv file\n```bash\n    soduco_geonetwork_cli update\n```\nUpdate records on Geonetwork\n```bash\n    soduco_geonetwork_cli update-postponed-values\n```\nUpdate records on Geonetwork based on a csv file containing postponed values at record creation (like links beetween records)",
    'author': 'Dumenieu Bertrand',
    'author_email': 'bertrand.dumenieu@ehess.fr',
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
