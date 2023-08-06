# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['oregpt']

package_data = \
{'': ['*']}

install_requires = \
['openai>=0.27.6,<0.28.0', 'prompt-toolkit>=3.0.38,<4.0.0', 'pyyaml>=6.0,<7.0']

entry_points = \
{'console_scripts': ['oregpt = oregpt.main:main']}

setup_kwargs = {
    'name': 'oregpt',
    'version': '0.1.0',
    'description': 'A tiny GPT CLI tool',
    'long_description': '# oregpt\nA tiny GPT CLI tool.\nYou can chat with the GPT model developped by OpenAI and save the conversation as json.\n\n![workflow](https://github.com/shinichi-takayanagi/oregpt/actions/workflows/main.yml/badge.svg)\n[![license](https://img.shields.io/github/license/shinichi-takayanagi/oregpt.svg)](https://github.com/shinichi-takayanagi/oregpt/blob/master/LICENSE)\n[![release](https://img.shields.io/github/release/shinichi-takayanagi/oregpt.svg)](https://github.com/shinichi-takayanagi/oregpt/releases/latest)\n[![python-version](https://img.shields.io/pypi/pyversions/oregpt.svg)](https://pypi.org/project/oregpt/)\n[![pypi](https://img.shields.io/pypi/v/oregpt?color=%2334D058&label=pypi%20package)](https://pypi.org/project/oregpt)\n\n![oregpt](https://user-images.githubusercontent.com/24406372/236361796-4a38af2b-b7b6-48e3-8ab6-dcba0be1532f.gif)\n\n## Installation\n### Get your own OpenAI API Key\nAssuming you have an environment variable with key named `OPENAI_API_KEY`.\nIf you don\'t have a OpenAI API key [visit here](https://platform.openai.com/account/api-keys), generate one and add it as an environment variable\n\n```bash\nexport OPENAI_API_KEY=<YOUR-OPENAI-API-KEY>\n\n```\n\n### Instal from PyPI\nYou can install the package using pip:\n\n```bash\n$ pip install oregpt\n```\n\n## Usage\nOnce you have installed oregpt, you can run it by typing:\n```bash\n$ oregpt\n```\n\n## Configuration\nYou can specify the place of conversation `log` , style (color etc) and the model provided by OpenAI in `~/.oregpt/config.yml`\n```\n❯ cat ~/.oregpt/config.yml\nlog: /tmp/oregpt/\nopenai:\n    model: gpt-3.5-turbo\n# You can also specify OpenAI\'s API key here\n#     api_key: <your-api-key>\nstyle:\n    user: "#00BEFE"\n    assistant: "#87CEEB"\n    system: "#cc0000"\n```\n',
    'author': 'Shinichi Takayanagi',
    'author_email': 'shinichi.takayanagi@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/shinichi-takayanagi/oregpt',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
