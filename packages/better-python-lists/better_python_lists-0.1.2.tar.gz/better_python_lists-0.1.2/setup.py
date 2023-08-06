# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['better_python_lists']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'better-python-lists',
    'version': '0.1.2',
    'description': 'Adds some useful methods on top of Python lists',
    'long_description': '# Better Python Lists\n\nMakes lists in Python better, by adding some useful methods.\n\n## Installation\n\n`pip install better-python-lists`\n\n## Basic Usage\n\n### Compact\n\nThe `compact` method is inspired by\n[Ruby\'s `Array.compact`](https://ruby-doc.org/core-3.0.0/Array.html#method-i-compact).\nIt removes all `None` elements from the List, returning a copy of the List.\n\n```py\nfrom better_python_lists import List\n\nmy_list = List([1, None, 2, 3, 4, None, None, 5])\ncompact_list = my_list.compact()\nprint(compact_list)\n# => [1, 2, 3, 4, 5]\n```\n\nYou can also perform in-place compacting using the `compacted` method:\n\n```py\nprint(my_list)  # => [1, None, 2, 3, 4, None, None, 5]\nmy_list.compacted()\nprint(my_list)  # => [1, 2, 3, 4, 5]\n```\n\nIf you want to filter out more than just `None`, you can pass in an optional filter list:\n\n```py\nanother_list = List([1, "None", 2, None, 3, "N/A"])\nanother_list.compacted(filter_list=[None, "None", "N/A"])\nprint(another_list)  # => [1, 2, 3]\n```\n',
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
