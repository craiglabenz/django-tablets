from __future__ import unicode_literals
from distutils.core import setup
from setuptools import find_packages

from tablets import __project__, __version__


CLASSIFIERS = [
    "Framework :: Django",
    "Intended Audience :: Developers",
    "Programming Language :: Python",
]

INSTALL_REQUIRES = []

setup(
    name="tablets",
    packages=find_packages("tablets"),
    version=__version__,
    description="The ultimate database-driven Django template experience",
    url="https://github.com/craiglabenz/tablets",
    download_url="https://github.com/craiglabenz/tablets/tarball/{0}".format(__version__),
    keywords=["django", "templates", "database-templates"],
    classifiers=CLASSIFIERS,
    install_requires=INSTALL_REQUIRES,
    author="Craig Labenz",
    author_email="craig.labenz@gmail.com",
    license="MIT"
)
