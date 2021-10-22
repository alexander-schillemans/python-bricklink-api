from setuptools import setup

# read the contents of README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'python-bricklink-api',         
  packages=['bricklink', 'bricklink.models', 'bricklink.constants', 'bricklink.endpoints'],
  version = '0.3.0',
  license='GPL-3.0-or-later',
  description = 'Wrapper for the Bricklink API (v1)',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Alexander Schillemans',
  author_email = 'alexander.schillemans@lhs.global',
  url = 'https://github.com/alexanderlhsglobal/python-bricklink-api',
  download_url = 'https://github.com/alexanderlhsglobal/python-bricklink-api/archive/refs/tags/0.3.0.tar.gz',
  keywords = ['bricklink', 'brick', 'link', 'brick link', 'lego', 'api'],
  install_requires=[
          'requests',
          'requests_oauthlib'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Programming Language :: Python :: 3.6',
  ],
)