# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['netext',
 'netext.edge_rendering',
 'netext.edge_routing',
 'netext.geometry',
 'netext.layout_engines',
 'netext.rendering',
 'netext.shapes']

package_data = \
{'': ['*']}

install_requires = \
['bitarray>=2.6.2,<3.0.0',
 'cachetools>=5.3.0,<6.0.0',
 'grandalf>=0.7,<0.8',
 'mkdocstrings[python]>=0.20.0,<0.21.0',
 'networkx-stubs>=0.0.1,<0.0.2',
 'networkx[default]>=3.0,<4.0',
 'rich>=13,<14',
 'rtree>=1.0.1,<2.0.0',
 'shapely>=2.0.1,<3.0.0']

setup_kwargs = {
    'name': 'netext',
    'version': '0.1.0',
    'description': 'A graph (network) rendering library for the terminal.',
    'long_description': 'None',
    'author': 'Malte Klemm',
    'author_email': 'me@malteklemm.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
