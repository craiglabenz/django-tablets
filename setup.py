import os
import re
from setuptools import setup


# Borrowed from the infamous
# https://github.com/tomchristie/django-rest-framework/blob/master/setup.py
def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


# Borrowed from the infamous
# https://github.com/tomchristie/django-rest-framework/blob/master/setup.py
def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


# Borrowed from the infamous
# https://github.com/tomchristie/django-rest-framework/blob/master/setup.py
def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


version = get_version('tablets')


CLASSIFIERS = [
    "Framework :: Django",
    "Intended Audience :: Developers",
    "Programming Language :: Python",
]


INSTALL_REQUIRES = [
    "django-ace",
    "django-mptt",
    "django-jsonfield==1.0.1",
]

setup(
    name="tablets",
    packages=get_packages("tablets"),
    package_data=get_package_data("tablets"),
    version=version,
    description="The ultimate database-driven Django template experience",
    url="https://github.com/craiglabenz/tablets",
    download_url="https://github.com/craiglabenz/tablets/tarball/{0}".format(version),
    keywords=["django", "templates", "database-templates", "jinja2"],
    classifiers=CLASSIFIERS,
    install_requires=INSTALL_REQUIRES,
    author="Craig Labenz",
    author_email="craig.labenz@gmail.com",
    license="MIT"
)
