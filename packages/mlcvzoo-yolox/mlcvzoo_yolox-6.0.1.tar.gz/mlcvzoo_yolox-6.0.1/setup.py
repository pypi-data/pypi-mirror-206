# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mlcvzoo_yolox',
 'mlcvzoo_yolox.core',
 'mlcvzoo_yolox.data',
 'mlcvzoo_yolox.data.datasets',
 'mlcvzoo_yolox.evaluators',
 'mlcvzoo_yolox.exp',
 'mlcvzoo_yolox.third_party',
 'mlcvzoo_yolox.third_party.yolox',
 'mlcvzoo_yolox.third_party.yolox.exps',
 'mlcvzoo_yolox.third_party.yolox.models',
 'mlcvzoo_yolox.third_party.yolox.tools',
 'mlcvzoo_yolox.third_party.yolox.utils']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=20',
 'loguru',
 'mlcvzoo_base>=5.0,<6.0',
 'ninja',
 'nptyping>=2.0',
 'numpy>=1.19.2,!=1.19.5',
 'opencv-contrib-python>=4.5,<5.0,!=4.5.5.64',
 'opencv-python>=4.5,<5.0,!=4.5.5.64',
 'psutil',
 'pycocotools>=2.0.2',
 'related-mltoolbox>=1.0,<2.0',
 'tabulate',
 'tensorboard',
 'thop',
 'torch>=1.9',
 'torchvision>=0.10',
 'tqdm',
 'yaml-config-builder>=8,<9']

extras_require = \
{'onnx': ['onnx>=1.13.0', 'onnx-simplifier==0.4.10'],
 'tensorrt': ['nvidia-tensorrt==8.4.2.4']}

setup_kwargs = {
    'name': 'mlcvzoo-yolox',
    'version': '6.0.1',
    'description': 'MLCVZoo YOLOX Package',
    'long_description': '# MLCVZoo YOLOX\n\nThe MLCVZoo is an SDK for simplifying the usage of various (machine learning driven)\ncomputer vision algorithms. The package **mlcvzoo_yolox** is the wrapper module for\nthe [yolox Object Detector](https://github.com/Megvii-BaseDetection/YOLOX).\n\nFurther information about the MLCVZoo can be found [here](../README.md).\n\n## Install\n`\npip install mlcvzoo-yolox\n`\n\n## Technology stack\n\n- Python\n',
    'author': 'Maximilian Otten',
    'author_email': 'maximilian.otten@iml.fraunhofer.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://git.openlogisticsfoundation.org/silicon-economy/base/ml-toolbox/mlcvzoo',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
