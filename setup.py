from __future__ import unicode_literals
from distutils.core import setup
from setuptools import find_packages

from tablets import __project__, __version__

README = open("README.md").read()
CHANGES = open("CHANGES.md").read()


CLASSIFIERS = [
    "Framework :: Django",
    "Intended Audience :: Developers",
    "Programming Language :: Python",
]

setup(
    name=__project__.lower(),
    packages=[__project__.lower()],
    version=__version__,
    description="The ultimate database-driven Django template experience",
    long_description = (README + "\n" + CHANGES),
    url="https://github.com/craiglabenz/tablets",
    download_url="https://github.com/craiglabenz/tablets/tarball/0.1.1",
    keywords=["django", "templates", "database-templates"],
    classifiers=CLASSIFIERS,
    install_requires=open("requirements.txt").readlines(),
    author="Craig Labenz",
    author_email="craig.labenz@gmail.com",
    license="MIT"
)
