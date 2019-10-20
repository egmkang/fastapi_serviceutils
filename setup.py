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
    version='0.2.0',
    description='Utils for fastapi based services.',
    python_requires='==3.*,>=3.7.0',
    project_urls={
        'repository': 'https://github.com/skallfass/fastapi_serviceutils'
    },
    author='Simon Kallfass',
    author_email='skallfass@ouroboros.info',
    entry_points={
        'console_scripts': [
            'create_service = fastapi_serviceutils.cli.create_service:main'
        ]
    },
    packages=[
        'fastapi_serviceutils', 'fastapi_serviceutils.base',
        'fastapi_serviceutils.cli.template.{{cookiecutter.service_name}}.app',
        'fastapi_serviceutils.cli.template.{{cookiecutter.service_name}}.app.endpoints',
        'fastapi_serviceutils.cli.template.{{cookiecutter.service_name}}.tests',
        'fastapi_serviceutils.default_endpoints', 'fastapi_serviceutils.docs',
        'fastapi_serviceutils.external_resources',
        'fastapi_serviceutils.middlewares'
    ],
    package_data={
        'fastapi_serviceutils.cli.template.{{cookiecutter.service_name}}.app': [
            '*.yml'
        ],
        'fastapi_serviceutils': [
            'cli/template/*.json',
            'cli/template/{{cookiecutter.service_name}}/*.cfg',
            'cli/template/{{cookiecutter.service_name}}/*.md',
            'cli/template/{{cookiecutter.service_name}}/*.toml',
            'cli/template/{{cookiecutter.service_name}}/*.txt',
            'cli/template/{{cookiecutter.service_name}}/*.yaml',
            'cli/template/{{cookiecutter.service_name}}/*.yml',
            'cli/template/{{cookiecutter.service_name}}/docs/*.rst'
        ]
    },
    install_requires=[
        'aiofiles==0.*,>=0.4.0', 'cookiecutter==1.*,>=1.6.0',
        'email-validator==1.*,>=1.0.4', 'fastapi==0.*,>=0.42.0',
        'loguru==0.*,>=0.3.0', 'pyyaml==5.*,>=5.1.0', 'requests==2.*,>=2.22.0',
        'starlette-prometheus==0.*,>=0.3.0', 'toolz==0.*,>=0.10.0',
        'ujson==1.*,>=1.35.0', 'uvicorn==0.*,>=0.9.0'
    ],
    extras_require={
        'dev': [
            'autoflake==1.*,>=1.3.0', 'coverage==4.*,>=4.5.0',
            'coverage-badge==1.*,>=1.0.0', 'flake8==3.*,>=3.7.0',
            'ipython==7.*,>=7.8.0', 'isort==4.*,>=4.3.0', 'jedi==0.*,>=0.14.0',
            'neovim==0.*,>=0.3.1', 'pre-commit>=1.18.3',
            'pudb==2019.*,>=2019.1.0', 'pygments==2.*,>=2.4.0',
            'pytest==5.*,>=5.0.0', 'pytest-asyncio>=0.10', 'pytest-cov>=2',
            'pytest-xdist==1.*,>=1.30.0', 'sphinx>=2',
            'sphinx-autodoc-typehints>=1.6', 'sphinx-rtd-theme>=0.4.3',
            'yapf==0.*,>=0.27.0'
        ],
        'devs': [
            'autoflake==1.*,>=1.3.0', 'coverage==4.*,>=4.5.0',
            'coverage-badge==1.*,>=1.0.0', 'flake8==3.*,>=3.7.0',
            'ipython==7.*,>=7.8.0', 'isort==4.*,>=4.3.0', 'jedi==0.*,>=0.14.0',
            'neovim==0.*,>=0.3.1', 'pre-commit>=1.18.3',
            'pudb==2019.*,>=2019.1.0', 'pygments==2.*,>=2.4.0',
            'pytest==5.*,>=5.0.0', 'pytest-asyncio>=0.10', 'pytest-cov>=2',
            'pytest-xdist==1.*,>=1.30.0', 'sphinx>=2',
            'sphinx-autodoc-typehints>=1.6', 'sphinx-rtd-theme>=0.4.3',
            'yapf==0.*,>=0.27.0'
        ]
    },
)