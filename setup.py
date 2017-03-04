import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="HomematicPy",
    version="1.0",
    author="Jan Breuer",
    author_email="breuxi.innovations@gmail.com",
    description=("Easy Phyton Wrapper Library for Homematic Systems"),
    license="GNU",
    keywords="library homematic smarthome wrapper",
    url="http://github.com/Breuxi/HomematicPy",
    packages=['HomematicPy'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 5 - Production/Stable"
    ],
)
