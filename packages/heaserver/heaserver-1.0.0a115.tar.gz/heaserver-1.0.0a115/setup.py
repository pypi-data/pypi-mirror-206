"""
Documentation for setup.py files is at https://setuptools.readthedocs.io/en/latest/setuptools.html
"""

from setuptools import setup, find_namespace_packages

# Import the README.md file contents
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='heaserver',
      version='1.0.0a115',
      description='The server side of HEA.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://risr.hci.utah.edu',
      author='Research Informatics Shared Resource, Huntsman Cancer Institute, Salt Lake City, UT',
      author_email='Andrew.Post@hci.utah.edu',
      python_requires='>=3.10',
      package_dir={'': 'src'},
      packages=find_namespace_packages(where='src'),
      package_data={'heaserver.service': ['py.typed', 'jsonschemafiles/*']},
      install_requires=[
          'heaobject~=1.0.0a53',
          'aiohttp[speedups]~=3.8.3',
          'aiohttp-remotes~=1.2.0',
          'motor~=2.5.1',
          'tzlocal~=4.2',
          'uritemplate~=4.1.1',
          'accept-types~=0.4.1',
          'mongoquery~=1.3.6',
          'jsonschema~=4.17.3',
          'jsonmerge~=1.8.0',
          'requests>=2.27',
          'types-requests>=2.27',  # Should be set at same version as requests.
          'boto3==1.21.38',
          'botocore==1.24.38',
          'boto3-stubs[essential]==1.21.38',
          'botocore-stubs[essential]==1.24.38',
          'freezegun~=1.0.0',  # Need an old version of freezegun for https://github.com/spulec/freezegun/issues/437
          'regex~=2022.4.24',
          'aio-pika==8.1.0',
          'PyJWT==2.6.0',
          'simpleeval~=0.9.12'
      ],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: Implementation :: CPython',
          'Topic :: Software Development',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
          'Topic :: Scientific/Engineering :: Information Analysis',
          'Topic :: Scientific/Engineering :: Medical Science Apps.'
      ]
      )
