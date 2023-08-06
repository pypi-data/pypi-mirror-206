# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['seppmail_converter']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.12.2,<5.0.0',
 'click>=8.1.3,<9.0.0',
 'lxml>=4.9.2,<5.0.0',
 'requests>=2.30,<3.0']

entry_points = \
{'console_scripts': ['seppmail-converter = seppmail_converter.main:entry']}

setup_kwargs = {
    'name': 'seppmail-converter',
    'version': '0.1.10',
    'description': 'Decode SEPPMail emails into EML files',
    'long_description': '# SEPPMail Converter\n\nThis python tool allows you to convert [SEPPMail](https://www.seppmail.com/) encrypted email files (`html`) to `.eml` files.\n\n## Usage\n\n```\nUsage: seppmail-converter [OPTIONS] INPUT_FILE\n\nOptions:\n  -u, --username TEXT\n  -p, --password TEXT\n  -o, --output PATH\n  -f, --force          Skip SEPPMail input file validation\n  -d, --delete         Delete input file after conversion\n  -o, --overwrite      Overwrite output file if it exists\n  -e, --extract        Extract attachments from .eml file\n  -q, --quiet          Suppress all output except final path\n  -v, --version        Show the version and exit.\n  --help               Show this message and exit.\n```\n\nRelevant environment variables:\n\n| Name                | Description                    |\n|---------------------|--------------------------------|\n| `SEPPMAIL_USERNAME` | Email supplied during login    |\n| `SEPPMAIL_PASSWORD` | Password supplied during login |\n\nUnless specified, the script will place the output file next to the input file and name it after the original file.\n',
    'author': 'Daniel Malik',
    'author_email': 'daniel.malik@mhsp.solutions',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
