# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['converterpro']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'converterpro',
    'version': '0.1.2',
    'description': 'Python converter library',
    'long_description': '<!-- BEGIN INCLUDE -->\n# ConverterPro\n\nA python library to convert units and currencies\n\n![Hex.pm](https://img.shields.io/hexpm/l/apa?style=flat&color=brightgreen)\n![GitHub issues](https://img.shields.io/github/issues/oforiwaasam/converterpro)\n[![Build Status](https://img.shields.io/github/actions/workflow/status/oforiwaasam/converterpro/build.yml)](https://github.com/oforiwaasam/converterpro/actions/workflows/build.yml)\n[![Coverage Status](https://coveralls.io/repos/github/oforiwaasam/converterpro/badge.svg?branch=main)](https://coveralls.io/github/oforiwaasam/converterpro?branch=main)\n[![black](https://img.shields.io/badge/code%20style-black-000000)](https://github.com/psf/black)\n[![poetry](https://img.shields.io/badge/packaging-poetry-008adf)](https://python-poetry.org/)\n[![PyPI](https://img.shields.io/pypi/v/converterpro)](https://pypi.org/project/converterpro/)\n[![Deployment](https://img.shields.io/github/deployments/oforiwaasam/converterpro/github-pages?label=GitHub&nbsp;Pages)](https://oforiwaasam.github.io/converterpro)\n[![Documentation Status](https://readthedocs.org/projects/converterpro/badge/?version=latest)](https://converterpro.readthedocs.io/en/latest/?badge=latest)\n\n## 🔭 Overview\n\nThis python library will allow developers to easily incorporate conversions into their programs without having to write all the logic for it. The library currently has the following functionalities:\n\n## 📝 Features\n\n+ Weight conversion between Metric, Imperial and US Systems of Measurement\n  + Grams\n  + Milligrams\n  + Kilograms\n  + Metric Tonnes\n  + Imperial Tons\n  + US tons\n  + Pounds\n  + Ounces\n\n## 🛠️ Installation\n\n**converterpro** can be found on [PyPi](https://pypi.org/project/converterpro/0.1.1/) and hence can be installed with `pip`:\n\n```bash\npip install converterpro\n```\n\n## ⛯ Basic Usage\n\n```python3\n>>> from converterpro import weight_converter\n>>> my_gram = weight_converter.Gram(1.0)\n>>> my_gram.convert_to_kilograms()\n0.001\n```\n\n## 📝 Details\n\nThis library project is a pure python project using modern tooling. It uses a `Makefile` as a command registry, with the following commands:\n\n+ `make`: list available commands\n+ `make install`: install and build this library and its dependencies using `poetry`\n+ `make lint`: perform static analysis of this library with `ruff` and `black`\n+ `make format`: autoformat this library using `black` and `ruff`\n+ `make test`: run automated tests with `pytest`\n+ `make coverage`: run automated tests with `pytest` and collect coverage information\n<!-- END INCLUDE -->\n\n## 👩🏾\u200d💻👨🏾\u200d💻 Contributing\n\nPlease see [CONTRIBUTING](https://converterpro.readthedocs.io/en/latest/contributing/) for more information.\n\n## \U0001faaa License\n\nThis software is licensed under the Apache 2.0 license. Please see [LICENSE](https://converterpro.readthedocs.io/en/latest/license/) for more information.\n\n## 🙎🏾\u200d Author\n\nMain Maintainer: Lily Sam\n',
    'author': 'Lily Sam',
    'author_email': 'los2119@columbia.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'http://converterpro.readthedocs.io/',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
