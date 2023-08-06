# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mlcvzoo_tf_classification',
 'mlcvzoo_tf_classification.custom_block',
 'mlcvzoo_tf_classification.xception']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=20',
 'keras-preprocessing>=1',
 'keras>=2.6',
 'mlcvzoo_base>=5.0,<6.0',
 'nptyping>=2.0',
 'numpy>=1.19.2,!=1.19.5',
 'opencv-contrib-python>=4.5,<5.0,!=4.5.5.64,!=4.6.0.66,!=4.7.0.68',
 'opencv-python>=4.5,<5.0,!=4.5.5.64,!=4.6.0.66',
 'pandas>=1.3.3',
 'related-mltoolbox>=1.0,<2.0',
 'tensorflow-cpu>=2.6',
 'yaml-config-builder>=8,<9']

setup_kwargs = {
    'name': 'mlcvzoo-tf-classification',
    'version': '6.0.1',
    'description': 'MLCVZoo TF Classifcation Package',
    'long_description': '# MLCVZoo TF Classification\n\nThe MLCVZoo is an SDK for simplifying the usage of various (machine learning driven)\ncomputer vision algorithms. The package **mlcvzoo_tf_classification** is the wrapper module\nfor classification algorithms that are implemented using tensorflow.\n\nFurther information about the MLCVZoo can be found [here](../README.md).\n\n## Install\n`\npip install mlcvzoo-tf-classification\n`\n\n## Technology stack\n\n- Python\n',
    'author': 'Maximilian Otten',
    'author_email': 'maximilian.otten@iml.fraunhofer.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://git.openlogisticsfoundation.org/silicon-economy/base/ml-toolbox/mlcvzoo',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
