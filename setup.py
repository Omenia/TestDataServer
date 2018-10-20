import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "ultimateTestDataServer",
    version = "0.0.1",
    author = "Siili Salabs",
    author_email = "info@siili.com",
    description = "Simple and powerful test data server",
    license = "keksijotain",
    keywords = "example documentation tutorial",
    url = "http://packages.python.org/ultimateTestDataServer",
    packages=['source', 'tests'],
    install_requires = ['connexion', 'Flask', 'flake8', 'pytest'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
