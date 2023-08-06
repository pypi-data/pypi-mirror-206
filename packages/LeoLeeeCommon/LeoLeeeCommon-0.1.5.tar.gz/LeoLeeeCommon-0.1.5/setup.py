from setuptools import (
    setup, find_packages
)

from LeoLeeeCommon.version import VERSION

setup(name='LeoLeeeCommon',
  version=VERSION,
  description='leo leee common library',
  url='http://github.com/LeoLeeeCommon/LeoLeeeCommon',
  author='LeoLeee',
  author_email='493671495@qq.com',
  license='MIT',
  packages=find_packages(),
  install_requires=[
      'PyYAML',
      'sqlalchemy',
  ],
  zip_safe=False)
