#!/usr/bin/env python

"""The setup script."""

import codecs
import os
import re

from setuptools import setup, find_packages

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Other/Proprietary License': 'License :: Other/Proprietary License'
} %}

###################################################################

PACKAGES = []
META_PATH = os.path.join("{{cookiecutter.namespace}}", "{{cookiecutter.package_name}}", "__init__.py")

KEYWORDS = ['{{ cookiecutter.project_slug }}', ]
CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
{%- if cookiecutter.license in license_classifiers %}
    '{{ license_classifiers[cookiecutter.license] }}',
{%- endif %}
{%- if cookiecutter.license == 'Other/Proprietary License' %}
    'Private :: Do Not Upload',
{%- endif %}
    'Natural Language :: English',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
]

###################################################################

about = {}
with open(os.path.join("{{cookiecutter.namespace}}", "{{cookiecutter.package_name}}", "__init__.py")) as f:
    exec(f.read(), about)

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = "" 

setup_requirements = "" 

setup(
    name=about["__title__"],
    author=about["__author__"],
    author_email=about["__email__"],
    version=about["__version__"],
    description=about["__summary__"],
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/x-rst",
    {%- if cookiecutter.license in license_classifiers %}
    license=about["__license__"],
    {%- endif %}
    url=about["__url__"],
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    entry_points={
        'z3c.autoinclude.plugin': 'target=uvcsite',
    },
    install_requires=requirements,
    include_package_data=True,
    packages=find_packages(include=['{{ cookiecutter.project_slug }}']),
    setup_requires=setup_requirements,
    test_suite='tests',
    zip_safe=False,
)
