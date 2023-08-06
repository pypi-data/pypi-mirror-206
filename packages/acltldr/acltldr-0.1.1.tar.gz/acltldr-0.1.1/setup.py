# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['acltldr']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'requests>=2.29.0,<3.0.0',
 'schnitsum>=0.4.6,<0.5.0',
 'sienna>=0.2.2,<0.3.0',
 'tqdm>=4.65.0,<5.0.0']

entry_points = \
{'console_scripts': ['acltldr = acltldr.main:run']}

setup_kwargs = {
    'name': 'acltldr',
    'version': '0.1.1',
    'description': '',
    'long_description': '# ACLTLDR\n\nThis is a python-based CLI tool used to generate summaries for ACL conference papers on [this page](https://sotaro.io/tldrs).\n\n\n## Installation\n\n```\npip install acltldr\n```\n\n\n## Usage\n\nAn example command to generate summaries for the proceedings of EACL 2021.\nFollowing command will generate a jsonl file with all the data, and a markdown file for the post.\n\n```\nacltldr https://raw.githubusercontent.com/acl-org/acl-anthology/master/data/xml/2021.eacl.xml \\\n        ./ \\\n\t--prefix "2021.eacl" \\\n\t--use-gpu\n```\n',
    'author': 'sobamchan',
    'author_email': 'oh.sore.sore.soutarou@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
