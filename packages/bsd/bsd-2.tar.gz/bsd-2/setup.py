# This file is placed in the Public Domain.


"bsd is not berkely"


import os


from setuptools import setup


def read():
    return open("README.rst", "r").read()


setup(
    name="bsd",
    version="2",
    author="Bart Thate",
    author_email="thatebhj@gmail.com",
    url="http://github.com/thatebhj/bsd",
    description="bsd is not berkely",
    long_description=read(),
    long_description_content_type="text/x-rst",
    license="Public Domain",
    packages=["bsd"],
    zip_safe=True,
    include_package_data=True,
    scripts=[
             "bin/bsd",
            ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: Public Domain",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
     ],
)
