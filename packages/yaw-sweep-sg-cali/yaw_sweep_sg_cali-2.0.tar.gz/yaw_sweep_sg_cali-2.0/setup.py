from setuptools import setup
# read the contents of your README file

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(name='yaw_sweep_sg_cali',
version='2.0',
description='Package to perform the strain gauge calibration placed on wind turbine towers based on idling opeartions, so called, yaw sweeps', 
long_description = long_description,
long_description_content_type='text/markdown',
author='Bruno and Zahra',
author_email='brofa@dtu.dk',
packages=['yaw_sweep_sg_cali'],
# packages_data={'yaw_sweep_sg_cali':['Data/V52_1min_data/*.txt', 'Data/V52_50Hz_data/*.txt','Data/V52_inputs.txt']}
install_requires = [
          'matplotlib',
          'numpy',
          'pandas',
          'pathlib',
          'scipy',
          'mysqlclient'
          ]

)