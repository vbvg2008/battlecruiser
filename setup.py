import os
import re

from setuptools import find_packages, setup


def get_version():
    path = os.path.dirname(__file__)
    version_re = re.compile(r'''__version__ = ['"](.+)['"]''')
    with open(os.path.join(path, 'battlecruiser', '__init__.py')) as f:
        init = f.read()
    return version_re.search(init).group(1)


setup(name="battlecruiser",
      version=get_version(),
      author="XMD",
      description="deep learning library",
      long_description="This is a deep learning library, not a run-of-the-mill battlecruiser.",
      url="https://github.com/flarahome/battlecruiser",
      license="Apache License 2.0",
      packages=find_packages(),
      classifiers=["License :: OSI Approved :: Apache Software License", "Programming Language :: Python :: 3"],
      python_requires='>=3.6')
