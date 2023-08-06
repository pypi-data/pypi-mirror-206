# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pypushover_logger']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pypushover-logger',
    'version': '0.1.0',
    'description': 'A Pushover logging handler',
    'long_description': 'pypushover-logger\n=================\n\nA simple logging handler that will push notification to Pushover.\n\nAll credits goes to: https://gist.github.com/snorrelo/28ab89d142ea93d363a34a8ce115b7cf\n\nThe code hosted here is simply a packaged and black-ed version of the code above.',
    'author': 'Jeffrey Muller',
    'author_email': 'jeffrey.muller92@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
