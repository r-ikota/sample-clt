from setuptools import setup
import os, sys
files = [os.path.join('printdata', 'data', 'salut.txt')]
setup(name='printdata',
      version='0.1.0',
      description="to test data files",

      url='https://github.com/r-ikota',
      packages=['printdata'],
      package_dir={'printdata': 'printdata'},
      data_files=[
        (os.path.join('printdata', 'data'), files)
      ],
      author='Ryo IKOTA',
      author_email='r.ikota.mt@gmail.com',
      entry_points={
        'console_scripts': [
            'pdata=printdata:pdata',
            'salut=printdata:salut'
        ],
      },
      license='BSD',
      keywords='data file'

      )
