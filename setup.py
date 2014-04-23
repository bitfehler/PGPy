from distutils.core import setup
from pip.req import parse_requirements

import pgpy._author

import os

# long_description is the contents of README.rst
with open('README.rst') as readme:
    long_desc = readme.read()

# requirements generators
reqs = parse_requirements('requirements.txt')
test_reqs = parse_requirements('requirements-test.txt')

##TODO: fill in blank fields
setup(
    name             = 'PGPy',
    version          = pgpy._author.__version__,
    description      = 'Pretty Good Privacy for Python',
    long_description = long_desc,
    author           = pgpy._author.__author__,
    license          = pgpy._author.__license__,
    url              = "https://github.com/Commod0re/PGPy",
    download_url     = "",

    classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Security',
        'Topic :: Security :: Cryptography',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
    ],
    keywords    = [],

    install_requires = [ str(ir.req) for ir in reqs ],

    packages = [
        "pgpy",
    ],
)