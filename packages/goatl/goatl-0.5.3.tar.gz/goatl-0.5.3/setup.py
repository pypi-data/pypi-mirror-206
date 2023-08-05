# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['goatl']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'goatl',
    'version': '0.5.3',
    'description': 'Greatest of all time logger',
    'long_description': '# goatl\n\n```\nsome body please prompt midjourney for "Cartoonish goat scribing on a long scroll oil painting, --ar  2:1"\nand make abanner for here.\n```\n##\n\n\n<div align="center">\n\n[![Build status](https://github.com/EytanDn/goatl/workflows/build/badge.svg?branch=master&event=push)](https://github.com/EytanDn/goatl/actions?query=workflow%3Abuild)\n[![Python Version](https://img.shields.io/pypi/pyversions/goatl.svg)](https://pypi.org/project/goatl/)\n[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/EytanDn/goatl/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/EytanDn/goatl/blob/master/.pre-commit-config.yaml)\n![Coverage Report](assets/images/coverage.svg)\n\nGreatest of all time logger\n\n</div>\n\n## Installation\n\n```bash\npip install -U goatl\n```\n\nor install with `Poetry`\n\n```bash\npoetry add goatl\n```\n\n## Releases\n\nYou can see the list of available releases on the [GitHub Releases](https://github.com/EytanDn/goatl/releases) page.\n\n## License\n\n[![License](https://img.shields.io/github/license/Eytandn/goatl)](https://github.com/EytanDn/goatl/blob/master/LICENSE)\n\nThis project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/eytandn/goatl/blob/master/LICENSE) for more details.\n\n## Citation\n\n```bibtex\n@misc{goatl,\n  author = {goatl},\n  title = {Greatest of all time logger},\n  year = {2023},\n  publisher = {GitHub},\n  journal = {GitHub repository},\n  howpublished = {\\url{https://github.com/EytanDn/goatl}}\n}\n```\n',
    'author': 'goatl',
    'author_email': 'EytanDn@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/EytanDn/goatl',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
