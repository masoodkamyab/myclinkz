"""Python setup.py for myclinkz package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("myclinkz", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="myclinkz",
    version=read("myclinkz", "VERSION"),
    description="Awesome myclinkz created by masoodkamyab",
    url="https://github.com/masoodkamyab/myclinkz/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="masoodkamyab",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["myclinkz = myclinkz.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
