# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')

setup(
    long_description=readme,
    name='fastapi_serviceutils',
    version='2.0.0',
    description='Utils for fastapi based services.',
    python_requires='<4,>=3.7',
    project_urls={
        'homepage': 'https://fastapi-serviceutils.readthedocs.io/en/latest/',
        'repository': 'https://github.com/skallfass/fastapi_serviceutils'
    },
    author='Simon Kallfass',
    author_email='skallfass@ouroboros.info',
    license='MIT',
    keywords='python fastapi webservice service-utils',
    classifiers=[
        'Operating System :: Unix', 'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7'
    ],
    entry_points={
        'console_scripts': [
            'create_service = fastapi_serviceutils.cli.create_service:main'
        ]
    },
    packages=[
        'fastapi_serviceutils', 'fastapi_serviceutils.app',
        'fastapi_serviceutils.app.endpoints',
        'fastapi_serviceutils.app.endpoints.default',
        'fastapi_serviceutils.app.handlers',
        'fastapi_serviceutils.app.middlewares', 'fastapi_serviceutils.cli',
        'fastapi_serviceutils.utils', 'fastapi_serviceutils.utils.docs',
        'fastapi_serviceutils.utils.external_resources',
        'fastapi_serviceutils.utils.tests'
    ],
    package_data={},
    install_requires=[
        'backoff>=1.8', 'cookiecutter>=1.6', 'databases[postgresql]>=0.2',
        'fastapi[all]>=0.42', 'loguru>=0.3', 'psycopg2>=2.8',
        'requests>=2.22.0', 'sqlalchemy>=1.3', 'toolz>=0.10'
    ],
    extras_require={
        'devs': [
            'autoflake>=1.3', 'coverage-badge>=1', 'flake8>=3.7',
            'ipython>=7.8', 'isort>=4.3', 'jedi>=0.14', 'neovim>=0.3.1',
            'pre-commit>=1.18.3', 'pudb>=2019.1', 'pygments>=2.4', 'pytest>=5',
            'pytest-asyncio>=0.10', 'pytest-cov>=2', 'pytest-xdist>=1.30',
            'sphinx>=2', 'sphinx-autodoc-typehints>=1.6',
            'sphinx-rtd-theme>=0.4.3', 'yapf>=0.27'
        ],
        'dev': [
            'autoflake>=1.3', 'coverage-badge>=1', 'flake8>=3.7',
            'ipython>=7.8', 'isort>=4.3', 'jedi>=0.14', 'neovim>=0.3.1',
            'pre-commit>=1.18.3', 'pudb>=2019.1', 'pygments>=2.4',
            'pylint>=2.4.3', 'pytest>=5', 'pytest-asyncio>=0.10',
            'pytest-cov>=2', 'pytest-xdist>=1.30', 'sphinx>=2',
            'sphinx-autodoc-typehints>=1.6', 'sphinx-rtd-theme>=0.4.3',
            'yapf>=0.27'
        ]
    },
)
