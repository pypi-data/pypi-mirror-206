# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['leap_model_parser',
 'leap_model_parser.contract',
 'leap_model_parser.utils',
 'leap_model_parser.utils.layerpedia',
 'leap_model_parser.utils.tlinspection',
 'leap_model_parser.utils.uicomponents']

package_data = \
{'': ['*']}

install_requires = \
['keras-data-format-converter==0.1.15.dev1',
 'leap-model-rebuilder==0.1.6.dev2',
 'numpy>=1.22.3,<2.0.0',
 'onnx2kerastl==0.0.84.dev1',
 'onnx==1.10.1']

extras_require = \
{':platform_machine == "arm64"': ['tensorflow-macos==2.12.0'],
 ':platform_machine == "x86_64"': ['tensorflow==2.12.0']}

entry_points = \
{'console_scripts': ['update_ui_components = '
                     'scripts.scripts:update_ui_components']}

setup_kwargs = {
    'name': 'leap-model-parser',
    'version': '0.1.93.dev2',
    'description': '',
    'long_description': '# Tensorleap model parser\nUsed to parse model to the import format \n',
    'author': 'idan',
    'author_email': 'idan.yogev@tensorleap.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/tensorleap/leap-model-parser',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
