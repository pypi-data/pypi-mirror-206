# (C) Copyright IBM Corporation 2019, 2020, 2021, 2022
# U.S. Government Users Restricted Rights:  Use, duplication or disclosure restricted
# by GSA ADP Schedule Contract with IBM Corp.

from setuptools import setup

setup(name='dscustom-libs',
      version='0.2',
      description='Often used functions in Digital Smelter project',
      url='https://github.com/luisgustavob78/dscustom-libs',
      author='Luis Gustavo Silva Barros',
      author_email='luisgustavob78@gmail.com',
      license='MIT',
      packages=['TSDataProcessing',
                'TSFeatures'],
      zip_safe=False)