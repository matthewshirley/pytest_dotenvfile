from os import path

from setuptools import setup

description = "Pytest plugin to load and parse dotenv files via the CLI"

setup(
    name="pytest_dotenvfile",
    description=description,
    version="0.5.2",
    author="Matt Shirley",
    author_email="mattshirley@hey.com",
    packages=["pytest_dotenvfile"],
    entry_points={"pytest11": ["dotenv = pytest_dotenvfile.plugin"]},
    install_requires=["pytest>=5.0.0", "python-dotenv>=0.9.1"],
    classifiers=[
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
)
