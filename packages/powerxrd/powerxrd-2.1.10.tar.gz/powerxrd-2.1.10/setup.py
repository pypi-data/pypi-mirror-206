# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['powerxrd']

package_data = \
{'': ['*']}

install_requires = \
['lmfit>=1.1.0,<2.0.0',
 'matplotlib>=3.6.3,<4.0.0',
 'numpy>=1.24.1,<2.0.0',
 'pandas>=1.5.3,<2.0.0',
 'scipy>=1.10.0,<2.0.0']

setup_kwargs = {
    'name': 'powerxrd',
    'version': '2.1.10',
    'description': 'Simple tools to handle powder XRD (and XRD) data with Python.',
    'long_description': '# powerxrd\nA Python package made to handle powder XRD (and XRD) data. \nThe only known open-source Github project with a Rietveld refinement method in development. \n\n<img src="https://raw.githubusercontent.com/andrewrgarcia/powerxrd/main/powerxrd.svg" width="400">\n\n\n## Installation\n\n```bash\npip install powerxrd\n```\n\n## Just starting? Check out the below options\n\n<a href="https://powerxrd.readthedocs.io/en/latest">\n<img src="https://raw.githubusercontent.com/andrewrgarcia/voxelmap/main/docs/img/readthedocs.png?raw=true" width="250" ></a>\n\n<a href="https://colab.research.google.com/drive/1_Eq-cW6LSPPnaRjkbeHaC81Wfbd8mQS-?usp=sharing">\n<img src="https://raw.githubusercontent.com/andrewrgarcia/powerxrd/main/docs/img/colaboratory.svg?raw=true" width="300" ></a>\n\n\n## Contributing\n\n1. Fork it (<https://github.com/your-github-user/powerxrd/fork>)\n2. Create your feature branch (`git checkout -b my-new-feature`)\n3. Commit your changes (`git commit -am \'Add some feature\'`)\n4. Push to the branch (`git push origin my-new-feature`)\n5. Create a new Pull Request\n\n',
    'author': 'andrewrgarcia',
    'author_email': 'garcia.gtr@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
