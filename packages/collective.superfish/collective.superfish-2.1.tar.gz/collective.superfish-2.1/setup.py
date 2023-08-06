# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

import os


def read(*pathnames):
    return open(os.path.join(os.path.dirname(__file__), *pathnames)).read()


setup(
    name='collective.superfish',
    version='2.1',
    description="A suckerfish/superfish integration into plone",
    long_description='\n'.join([
        read('README.rst'),
        read('docs', 'TODO.txt'),
        read('docs', 'THANKS.txt'),
        read('CHANGES.rst'),
    ]),
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: Addon",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords='navigation suckerfish superfish jquery dropdown',
    author='Peter Mathis',
    author_email='peter.mathis@kombinat.at',
    url='https://github.com/collective/collective.superfish',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
