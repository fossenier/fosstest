# setup.py for Logan Fossenier's testing utilities

from setuptools import setup, find_packages

setup(
    name="fosstest",
    version="0.1.0",
    author="Logan Fossenier",
    author_email="logan.fossenier@gmail.com",
    description="Testing utilities to make writing tests easier.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
