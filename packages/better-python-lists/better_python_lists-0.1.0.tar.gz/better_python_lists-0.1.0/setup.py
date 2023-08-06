# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['better_python_lists']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'better-python-lists',
    'version': '0.1.0',
    'description': 'Adds some useful methods on top of Python lists',
    'long_description': '# better-python-lists\nAdds some useful methods on top of Python lists\n',
    'author': 'Bradley Marques',
    'author_email': 'bradleyrcmarques@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
