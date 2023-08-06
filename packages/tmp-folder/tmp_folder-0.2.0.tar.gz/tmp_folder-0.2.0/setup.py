# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tmp_folder']

package_data = \
{'': ['*']}

install_requires = \
['typing-extensions>=4.0.1,<5.0.0']

setup_kwargs = {
    'name': 'tmp-folder',
    'version': '0.2.0',
    'description': 'Extends python `TemporaryDirectory` and make it even easier to use, as a decorator.',
    'long_description': '<p align="center">\n  <img src="https://raw.githubusercontent.com/jalvaradosegura/tmp-folder/main/docs/tmp-folder.png" alt="tmp-folder">\n</p>\n\n<p align="center">\n\n  <a href="https://codecov.io/gh/jalvaradosegura/tmp-folder">\n    <img src="https://codecov.io/gh/jalvaradosegura/tmp-folder/branch/main/graph/badge.svg?token=IL5PVTYVRV"/>\n  </a>\n\n  <a href="https://github.com/psf/black" target="_blank">\n    <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="black">\n  </a>\n\n  <a href="https://pycqa.github.io/isort/" target="_blank">\n    <img src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336" alt="isort">\n  </a>\n\n  <a href="https://github.com/jalvaradosegura/tmp-folder/actions/workflows/unit_tests.yml" target="_blank">\n    <img src="https://github.com/jalvaradosegura/tmp-folder/actions/workflows/unit_tests.yml/badge.svg" alt="License">\n  </a>\n\n  <a href="https://pepy.tech/project/tmp-folder" target="_blank">\n    <img src="https://static.pepy.tech/personalized-badge/tmp-folder?period=total&units=international_system&left_color=grey&right_color=blue&left_text=downloads" alt="downloads">\n  </a>\n\n  <a href="https://www.instagram.com/circus.infernus/" target="_blank">\n    <img src="https://img.shields.io/badge/image--by-%40circus.infernus-blue" alt="image-by">\n  </a>\n\n</p>\n\n---\n\nDocumentation: https://jalvaradosegura.github.io/tmp-folder/\n\n---\n\n## tmp-folder\nEasily create a temporary folder. Put files in it and after you\'re done tmp-folder will delete the folder automatically.\n\n## Installation\n\nInstall from PyPI:\n\n```\npip install tmp-folder\n```\n\n## Usage\nThis is the minimum you need to get started with `tmp-folder`:\n```py\nfrom pathlib import Path\n\nfrom tmp_folder import use_tmp_folder\n\n\n@use_tmp_folder\ndef foo(tmp_folder: Path):\n    pass\n```\n\nJust decorate the function in which you need a temporary folder. Then add as first parameter, the variable that will hold the temporary folder path (it can be named however you want). Finally, after the function execution is completed, the folder will be deleted.\n',
    'author': 'Jorge Alvarado',
    'author_email': 'alvaradosegurajorge@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://jalvaradosegura.github.io/tmp-folder/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
